# Publish Package

This GitHub Action builds Python packages and publishes them to PyPI (Python Package Index). It automates the entire package publishing workflow, from building distributions to uploading them to PyPI.

## Features

- 📦 **Package Building**: Automatically builds source and wheel distributions
- 🚀 **PyPI Publishing**: Uploads packages to PyPI with proper authentication
- ✅ **Distribution Validation**: Checks built distributions before publishing
- 🔒 **Secure Authentication**: Uses PyPI credentials for secure uploads
- 🔄 **Skip Existing**: Prevents duplicate uploads with `--skip-existing`
- 🛠️ **Modern Tooling**: Uses `build` and `twine` for reliable packaging

## Usage

### Basic Usage

```yaml
- name: Publish Package
  uses: ./actions/python/publish-package
  with:
    pypi-url: https://upload.pypi.org/legacy/
    pypi-user-name: ${{ secrets.PYPI_USERNAME }}
    pypi-secret: ${{ secrets.PYPI_PASSWORD }}
```

### TestPyPI Publishing

```yaml
- name: Publish to TestPyPI
  uses: ./actions/python/publish-package
  with:
    pypi-url: https://test.pypi.org/legacy/
    pypi-user-name: ${{ secrets.TEST_PYPI_USERNAME }}
    pypi-secret: ${{ secrets.TEST_PYPI_PASSWORD }}
```

## Input Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `pypi-url` | PyPI repository URL | ✅ |
| `pypi-user-name` | PyPI username | ✅ |
| `pypi-secret` | PyPI password or API token | ✅ |

## PyPI URLs

### Production PyPI

```text
https://upload.pypi.org/legacy/
```

### Test PyPI

```text
https://test.pypi.org/legacy/
```

### Private PyPI (Nexus, DevPI, etc.)

```text
https://your-private-pypi.com/simple/
```

## Workflow Integration

### Complete Release Workflow

```yaml
name: Release Package
on:
  push:
    tags:
      - 'v*'

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Publish Package
        uses: ./actions/python/publish-package
        with:
          pypi-url: https://upload.pypi.org/legacy/
          pypi-user-name: ${{ secrets.PYPI_USERNAME }}
          pypi-secret: ${{ secrets.PYPI_PASSWORD }}
```

### TestPyPI Workflow

```yaml
name: Test Release
on:
  push:
    branches: [main]

jobs:
  test-publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Publish to TestPyPI
        uses: ./actions/python/publish-package
        with:
          pypi-url: https://test.pypi.org/legacy/
          pypi-user-name: ${{ secrets.TEST_PYPI_USERNAME }}
          pypi-secret: ${{ secrets.TEST_PYPI_PASSWORD }}
```

## PyPI Authentication Setup

### Using Username and Password

1. **Create PyPI account** at [pypi.org](https://pypi.org)
2. **Add secrets** to your GitHub repository:
   - `PYPI_USERNAME`: Your PyPI username
   - `PYPI_PASSWORD`: Your PyPI password

### Using API Tokens (Recommended)

1. **Generate API token** in PyPI account settings
2. **Add secrets** to your GitHub repository:
   - `PYPI_USERNAME`: `__token__`
   - `PYPI_PASSWORD`: Your API token (starts with `pypi-`)

### TestPyPI Setup

1. **Create TestPyPI account** at [test.pypi.org](https://test.pypi.org)
2. **Add secrets**:
   - `TEST_PYPI_USERNAME`: Your TestPyPI username
   - `TEST_PYPI_PASSWORD`: Your TestPyPI password or API token

## Package Configuration

### pyproject.toml

Your package should have a proper `pyproject.toml` configuration:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel", "build"]
build-backend = "setuptools.build_meta"

[project]
name = "your-package-name"
version = "1.0.0"
description = "Your package description"
authors = [{name = "Your Name", email = "your.email@example.com"}]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.8"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]

[project.urls]
Homepage = "https://github.com/yourusername/your-package"
Repository = "https://github.com/yourusername/your-package"
Issues = "https://github.com/yourusername/your-package/issues"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-dir]
"" = "src"
```

### Directory Structure

```text
project/
├── src/
│   └── your_package/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── README.md
├── LICENSE
└── pyproject.toml
```

## What the Action Does

1. **Installs dependencies**: Uses `uv` to install build tools
2. **Builds package**: Runs `python -m build` to create distributions
3. **Validates distributions**: Runs `twine check` to verify package integrity
4. **Publishes package**: Uploads to PyPI using `twine upload`
5. **Skips existing**: Uses `--skip-existing` to prevent duplicate uploads

## Dependencies

The action uses the following Python packages:

- `build`: Modern Python package builder
- `setuptools>=61.0`: Package building backend
- `wheel`: Wheel distribution format
- `twine`: Secure package uploader

## Troubleshooting

### Common Issues

1. **Authentication errors**: Verify PyPI credentials are correct
2. **Package already exists**: Use `--skip-existing` flag (already included)
3. **Build errors**: Check `pyproject.toml` configuration
4. **Permission errors**: Ensure API token has upload permissions

### Debug Mode

To debug the publishing process, you can run the commands manually:

```bash
# Build package
python -m build

# Check distributions
twine check dist/*

# Upload to PyPI
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

### Validation Commands

```bash
# Check package configuration
python -m build --sdist --wheel

# Validate distributions
twine check dist/*

# Test upload (dry run)
twine upload --repository-url https://test.pypi.org/legacy/ --skip-existing dist/*
```

## Best Practices

### Package Versioning

1. **Use semantic versioning**: Follow `MAJOR.MINOR.PATCH` format
2. **Update version**: Increment version in `pyproject.toml` before release
3. **Tag releases**: Use Git tags for version tracking
4. **Changelog**: Maintain a changelog for version history

### Security

1. **Use API tokens**: Prefer API tokens over passwords
2. **Limit token scope**: Use tokens with minimal required permissions
3. **Rotate credentials**: Regularly update API tokens
4. **Secure secrets**: Never commit credentials to code

### Quality Assurance

1. **Test before publish**: Run tests and linting before publishing
2. **Use TestPyPI**: Test publishing process on TestPyPI first
3. **Validate distributions**: Always check built packages
4. **Review package info**: Verify package metadata before publishing

## Release Workflow Example

```yaml
name: Release
on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements-dev.txt

      - name: Run tests
        run: pytest tests/

      - name: Run linting
        run: ruff check src/

      - name: Publish Package
        uses: ./actions/python/publish-package
        with:
          pypi-url: https://upload.pypi.org/legacy/
          pypi-user-name: ${{ secrets.PYPI_USERNAME }}
          pypi-secret: ${{ secrets.PYPI_PASSWORD }}
```

## License

This project is licensed under the same license as the main repository.
