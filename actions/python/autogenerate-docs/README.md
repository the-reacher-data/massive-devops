# Docs Build & Deploy

This GitHub Action automatically generates Sphinx documentation from your Python source code and deploys it to GitHub Pages for releases or uploads artifacts for PR previews.

## Features

- 📚 **Automatic API documentation**: Generates API docs using `sphinx-apidoc`
- 🏗️ **Sphinx HTML build**: Builds complete HTML documentation
- 🔗 **GitHub Pages deployment**: Automatically deploys docs on releases
- 📦 **Artifact upload**: Uploads docs artifacts for PR previews
- 🔧 **Symlink normalization**: Handles symlinks and hardlinks properly
- 🎨 **Modern theme**: Uses Furo theme for beautiful documentation

## Usage

### Release Mode (Deploy to GitHub Pages)

Deploy documentation to GitHub Pages when creating a release:

```yaml
- name: Build and Deploy Documentation
  uses: ./actions/python/autogenerate-docs
  with:
    mode: release
    src-dir: src
    docs-dir: docs
```

### PR Mode (Upload Artifact)

Generate documentation and upload as artifact for PR previews:

```yaml
- name: Build Documentation Preview
  uses: ./actions/python/autogenerate-docs
  with:
    mode: pr
    src-dir: src
    docs-dir: docs
```

## Input Parameters

| Parameter | Description | Required | Default |
|-----------|-------------|----------|---------|
| `src-dir` | Path to source code directory (for sphinx-apidoc) | ❌ | `src` |
| `docs-dir` | Path to documentation directory | ❌ | `docs` |
| `mode` | Operation mode: `pr` or `release` | ✅ | - |

## Output Parameters

| Parameter | Description |
|-----------|-------------|
| `page-url` | URL of the deployed GitHub Pages site (only in release mode) |

## Documentation Structure

The action expects the following directory structure:

```bash
project/
├── src/ # Source code directory
│ └── your_package/
│ ├── init.py
│ └── modules.py
├── docs/ # Documentation directory
│ ├── conf.py # Sphinx configuration
│ ├── index.rst # Main documentation file
│ └── api/ # Auto-generated API docs (created by action)
└── pyproject.toml # Project configuration

```

## Sphinx Configuration

Your `docs/conf.py` should include the necessary extensions and settings:

```python
# conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser',
]

html_theme = 'furo'
html_static_path = ['_static']
```

## Workflow Integration

### Complete Release Workflow

```yaml
name: Release Documentation
on:
  push:
    tags:
      - 'v*'

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build and Deploy Documentation
        uses: ./actions/python/autogenerate-docs
        with:
          mode: release
          src-dir: src
          docs-dir: docs
```

### Complete PR Workflow

```yaml
name: Documentation Preview
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build Documentation Preview
        uses: ./actions/python/autogenerate-docs
        with:
          mode: pr
          src-dir: src
          docs-dir: docs

      - name: Upload Documentation Artifact
        uses: actions/upload-artifact@v4
        with:
          name: documentation-preview
          path: docs/_build/html/
          retention-days: 7
```

## GitHub Pages Setup

To enable GitHub Pages deployment, configure your repository settings:

1. Go to **Settings** → **Pages**
2. Set **Source** to "GitHub Actions"
3. Ensure the workflow has the required permissions:

   ```yaml
   permissions:
     contents: read
     pages: write
     id-token: write
   ```

## Dependencies

The action uses the following Python packages:

- `sphinx==8.2.3`: Documentation generator
- `furo==2025.7.19`: Modern Sphinx theme
- `myst-parser==4.0.1`: Markdown parser for Sphinx

## What the Action Does

1. **Installs dependencies**: Uses `uv` to install Sphinx and related packages
2. **Generates API docs**: Runs `sphinx-apidoc` to create API documentation from source code
3. **Builds HTML docs**: Runs `sphinx-build` to generate HTML documentation
4. **Normalizes links**: Removes symlinks and hardlinks to ensure proper artifact handling
5. **Deploys or uploads**:
   - In release mode: Deploys to GitHub Pages
   - In PR mode: Uploads as artifact for preview

## Customization

### Custom Sphinx Configuration

You can customize the Sphinx build by modifying your `docs/conf.py`:

```python
# conf.py
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

# Theme configuration
html_theme = 'furo'
html_theme_options = {
    "navigation_with_keys": True,
    "announcement": "Documentation generated automatically!",
}

# API documentation settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}
```

### Custom Source Directory

If your source code is in a different location:

```yaml
- name: Build Documentation
  uses: ./actions/python/autogenerate-docs
  with:
    mode: release
    src-dir: lib  # Custom source directory
    docs-dir: documentation  # Custom docs directory
```

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure your `docs/conf.py` includes the correct path to your source code
2. **Missing dependencies**: Check that all required packages are listed in `requirements.txt`
3. **Permission errors**: Verify GitHub Pages permissions are correctly set
4. **Build failures**: Check that your Sphinx configuration is valid

### Debug Mode

To debug documentation generation, you can run the commands manually:

```bash
# Generate API docs
sphinx-apidoc -o docs/api src --force

# Build HTML docs
sphinx-build -b html docs docs/_build/html
```

## License

This project is licensed under the same license as the main repository.
