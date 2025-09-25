# Workflow Examples

This directory contains **demo workflows** that show how to use the Massive DevOps workflows from external repositories.

## 🚨 Important Notice

> **⚠️ WARNING**: These are **demo workflows** that may not work out of the box. They are provided as examples of how to integrate Massive DevOps workflows into your project. You may need to adjust paths, secrets, and configurations for your specific project.

## 📋 Available Demo Workflows

### 1. Pre-Release Demo (`pre_release_demo.yaml`)

**Purpose**: Example of how to use the pre-release workflow for PR validation.

**Usage**: Copy this file to your repository's `.github/workflows/` directory and customize:

```yaml
# Copy to .github/workflows/pre_release.yml
name: Pre-Release Checks
on:
  pull_request:
    branches: [ "main" ]

jobs:
  pre-release-checks:
    uses: the-reacher-data/massive-devops/workflows/python/pre_release.yml@v1
    with:
      python-version: "3.12"
      src-dir: "src"                    # Adjust to your source directory
      test-dir: "tests"                 # Adjust to your test directory
      coverage-threshold: "80"           # Adjust to your requirements
      linter-fail-on: "any"             # Adjust failure conditions
      security-fail-on: "medium"        # Adjust security threshold
    secrets:
      pypi-secret: ${{ secrets.TEST_PYPI_API_TOKEN }}
      github-token: ${{ secrets.GITHUB_TOKEN }}
      codecov-token: ${{ secrets.CODECOV_TOKEN }}
```

### 2. Production Release Demo (`production_release_demo.yaml`)

**Purpose**: Example of how to use the production release workflow.

**Usage**: Copy this file to your repository's `.github/workflows/` directory and customize:

```yaml
# Copy to .github/workflows/production_release.yml
name: Production Release
on:
  push:
    branches: ["main"]

jobs:
  production-release:
    uses: the-reacher-data/massive-devops/workflows/python/production_release.yml@v1
    with:
      python-version: "3.12"
      pypi-url: "https://upload.pypi.org/legacy/"
      src-dir-docs: "src"               # Adjust to your source directory
      github-sha: ${{ github.sha }}
    permissions:
      contents: write
      pull-requests: read
      id-token: write
      pages: write
      security-events: write
      actions: read
    secrets:
      pypi-secret: ${{ secrets.PYPI_API_TOKEN }}
      github-token: ${{ secrets.GITHUB_TOKEN }}
      codecov-token: ${{ secrets.CODECOV_TOKEN }}
```

## 🔧 Customization Required

### 1. Directory Structure

Ensure your project follows this structure:

```text
your-python-project/
├── src/                    # Source code (adjust src-dir parameter)
|   └── tests/              # Test files (adjust test-dir parameter)
├── docs/                   # Documentation (optional)
├── pyproject.toml          # Project configuration
├── requirements.txt        # Dependencies
└── .github/
    └── workflows/          # Your workflow files
```

### 2. Required Secrets

Set up these secrets in your repository settings:

| Secret | Description | Required For |
|--------|-------------|--------------|
| `GITHUB_TOKEN` | GitHub token (usually provided automatically) | Both workflows |
| `PYPI_API_TOKEN` | PyPI API token for production releases | Production release |
| `TEST_PYPI_API_TOKEN` | TestPyPI token for pre-releases | Pre-release |
| `CODECOV_TOKEN` | Codecov token for coverage reporting | Both workflows (optional) |

### 3. Configuration Parameters

Adjust these parameters in the workflow files:

- **`src-dir`**: Path to your source code directory
- **`test-dir`**: Path to your test directory
- **`coverage-threshold`**: Minimum coverage percentage
- **`linter-fail-on`**: When to fail on linting issues (`any` or `none`)
- **`security-fail-on`**: Security threshold (`none`, `low`, `medium`, `high`)
- **`python-version`**: Python version to use

## 🚀 Quick Start

1. **Fork or clone** this repository
2. **Copy** the demo workflow files to your project
3. **Customize** the parameters for your project
4. **Set up** the required secrets
5. **Test** with a small change first

## 📚 Documentation

- **Main README**: [../README.md](../README.md) - Complete project documentation
- **Python Workflows**: [../python/README.md](../python/README.md) - Detailed workflow documentation
- **Actions**: [../../actions/](../../actions/) - Individual action documentation

## 🤝 Contributing

When contributing to these demo workflows:

1. **Test thoroughly**: Ensure examples work with different project structures
2. **Update documentation**: Keep this README current
3. **Follow conventions**: Use conventional commits
4. **Consider compatibility**: Ensure changes work for external users

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/the-reacher-data/massive-devops/issues)
- **Discussions**: [GitHub Discussions](https://github.com/the-reacher-data/massive-devops/discussions)

---

## Made with ❤️ for the Python community
