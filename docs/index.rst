Massive DevOps Documentation
=============================

A comprehensive collection of GitHub Actions designed for Python projects using **Trunk-Based Development** and **Conventional Commits**. This repository provides a complete DevOps toolkit that automates code quality, testing, security analysis, documentation generation, and package publishing.

.. note::
   **Status**: This project is currently in development but already functional. All actions are working and can be used in production environments.

Features
--------

- **Trunk-Based Development**: Optimized for continuous integration with main branch workflows
- **Conventional Commits**: Automatic changelog generation and semantic versioning
- **Complete Python Workflow**: From linting to publishing
- **Enterprise-Ready**: Professional reports with logos, badges, and detailed analysis
- **Modular Design**: Use individual actions or combine them for complete workflows

Quick Start
-----------

Basic Python Project Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   name: Python CI/CD
   on:
     push:
       branches: [main]
     pull_request:
       types: [opened, synchronize]

   jobs:
     quality:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4

         # Install dependencies
         - uses: ./actions/python/uv-requirements
           with:
             requirements: requirements.txt

         # Run linting and type checking
         - uses: ./actions/python/linter-comment
           with:
             src-dir: src
             github-token: ${{ secrets.GITHUB_TOKEN }}

         # Run tests with coverage
         - uses: ./actions/python/pytest-comment
           with:
             test-dir: tests
             src-dir: src
             github-token: ${{ secrets.GITHUB_TOKEN }}

         # Security analysis
         - uses: ./actions/python/security-comment
           with:
             src-dir: src
             github-token: ${{ secrets.GITHUB_TOKEN }}

Complete Release Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

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
           with:
             fetch-depth: 0

         # Generate changelog
         - uses: ./actions/devops/changelog-conventional-commit
           with:
             mode: release
             branch: main
             version: ${{ github.ref_name }}

         # Generate documentation
         - uses: ./actions/python/autogenerate-docs
           with:
             mode: release
             src-dir: src
             docs-dir: docs

         # Publish package
         - uses: ./actions/python/publish-package
           with:
             pypi-url: https://upload.pypi.org/legacy/
             pypi-user-name: ${{ secrets.PYPI_USERNAME }}
             pypi-secret: ${{ secrets.PYPI_PASSWORD }}

Actions Overview
================

DevOps Actions
--------------

.. toctree::
   :maxdepth: 1

   changelog-conventional-commit <actions/devops/changelog-conventional-commit/README.md>
   pr-comment-update <actions/devops/pr-comment-update/README.md>
   versioning-branch-semantic <actions/devops/versioning-branch-semantic/README.md>

Python Actions
--------------

.. toctree::
   :maxdepth: 1

   autogenerate-docs <actions/python/autogenerate-docs/README.md>
   linter-comment <actions/python/linter-comment/README.md>
   pytest-comment <actions/python/pytest-comment/README.md>
   security-comment <actions/python/security-comment/README.md>
   publish-package <actions/python/publish-package/README.md>
   uv-requirements <actions/python/uv-requirements/README.md>

Workflows
=========

Complete CI/CD Workflows
------------------------

This repository includes **two complementary workflows** designed to work together:

Pre-Release Workflow
~~~~~~~~~~~~~~~~~~~~

**Purpose**: Handles Pull Request validation and pre-release testing.

**Triggers**: Pull Request events (opened, synchronize)

**What it does**:
- 🧹 **Linting & Type Checking**: Runs Ruff + MyPy
- 🔒 **Security Analysis**: Runs Bandit security scanner
- 🧪 **Testing & Coverage**: Runs pytest with coverage analysis
- 📦 **Pre-release Publishing**: Publishes to TestPyPI (if deployable)
- 📚 **Documentation Preview**: Generates documentation preview
- 📝 **Changelog Preview**: Generates changelog from conventional commits

Production Release Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**: Handles production releases and deployment.

**Triggers**: Push to main branch (after PR merge)

**What it does**:
- 🔍 **Branch Detection**: Finds the original PR branch from squash commit
- 🧪 **Final Testing**: Runs tests on the merged code
- 📝 **Version Generation**: Creates semantic version based on branch name
- 📋 **Changelog Generation**: Creates release changelog from conventional commits
- 🚀 **Production Publishing**: Publishes to PyPI production
- 📚 **Documentation Deployment**: Deploys docs to GitHub Pages
- 🔖 **Git Tagging**: Creates version tags
- 🛡️ **CodeQL Analysis**: Runs security analysis

.. warning::
   These workflows are **complementary** and designed to work together. Using only one workflow may not provide complete functionality. For optimal results, use both workflows as part of your complete CI/CD pipeline.

Workflow Integration
~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   # .github/workflows/ci.yml
   name: CI/CD Pipeline

   on:
     pull_request:
       types: [opened, synchronize]
     push:
       branches: [main]

   jobs:
     pre-release:
       if: github.event_name == 'pull_request'
       uses: ./.github/workflows/python/pre_release.yml
       with:
         python-version: "3.11"
         src-dir: "src"
         test-dir: "tests"
         coverage-threshold: "85"
         linter-fail-on: "any"
         security-fail-on: "medium"
       secrets:
         github-token: ${{ secrets.GITHUB_TOKEN }}
         pypi-secret: ${{ secrets.TEST_PYPI_TOKEN }}
         codecov-token: ${{ secrets.CODECOV_TOKEN }}

     production-release:
       if: github.event_name == 'push' && github.ref == 'refs/heads/main'
       uses: ./.github/workflows/python/production_release.yml
       with:
         python-version: "3.11"
         src-dir: "src"
         test-dir: "tests"
         github-sha: ${{ github.sha }}
       secrets:
         github-token: ${{ secrets.GITHUB_TOKEN }}
         pypi-secret: ${{ secrets.PYPI_TOKEN }}
         codecov-token: ${{ secrets.CODECOV_TOKEN }}
       permissions:
         contents: write
         pages: write
         id-token: write

Configuration
=============

Project Structure
-----------------

.. code-block:: text

   your-python-project/
   ├── src/                    # Source code
   │   └── your_package/
   │       ├── __init__.py
   │       └── modules.py
   ├── tests/                  # Test files
   │   ├── test_main.py
   │   ├── test_utils.py
   │   └── test_api.py
   ├── docs/                   # Documentation
   │   ├── conf.py
   │   ├── index.rst
   │   └── api/               # Auto-generated API docs
   ├── .github/
   │   └── workflows/          # GitHub Actions workflows
   ├── pyproject.toml          # Project configuration
   └── README.md

pyproject.toml Example
----------------------

.. code-block:: toml

   [build-system]
   requires = ["setuptools>=61.0", "wheel", "build"]
   build-backend = "setuptools.build_meta"

   [project]
   name = "your-package"
   version = "1.0.0"
   description = "Your package description"
   requires-python = ">=3.8"

   [tool.ruff]
   line-length = 88
   target-version = "py38"

   [tool.ruff.lint]
   select = ["E", "F", "W", "I", "N", "UP", "B", "A", "C4", "T20"]

   [tool.mypy]
   python_version = "3.8"
   warn_return_any = true
   warn_unused_configs = true

   [tool.pytest.ini_options]
   testpaths = ["tests"]
   addopts = "-v --tb=short"

   [tool.coverage.run]
   source = ["src"]
   omit = ["tests/*"]

   [tool.bandit]
   exclude_dirs = ["tests", "migrations"]

Dependencies
============

Core Tools
----------

- **Python 3.8+**: All actions support modern Python versions
- **uv**: Fast Python package manager for dependency installation
- **Git**: Required for version control operations

Quality Tools
-------------

- **Ruff**: Fast Python linter and formatter
- **MyPy**: Static type checker
- **Bandit**: Security linter
- **pytest**: Testing framework
- **coverage**: Code coverage measurement

Documentation & Publishing
--------------------------

- **Sphinx**: Documentation generator
- **Furo**: Modern Sphinx theme
- **build**: Python package builder
- **twine**: Package uploader

Contributing
============

Development Workflow
--------------------

1. **Fork the repository**
2. **Create a feature branch** from `main`
3. **Make your changes** following our guidelines
4. **Create a Pull Request** with conventional commit format
5. **Wait for review** and merge approval

Branch Protection
-----------------

- **Main branch is protected**: Direct pushes to `main` are not allowed
- **Pull Requests required**: All changes must go through PRs
- **Squash merge only**: PRs are merged using squash merge to maintain clean history
- **Conventional Commits**: All commits must follow conventional commit format

Commit Guidelines
-----------------

All commits must follow the `Conventional Commits <https://www.conventionalcommits.org/>`_ specification:

.. code-block:: text

   <type>[optional scope]: <description>

   [optional body]

   [optional footer(s)]

Supported Types
~~~~~~~~~~~~~~~

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools
- `ci`: Changes to our CI configuration files and scripts
- `build`: Changes that affect the build system or external dependencies

Commit Examples
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Good examples
   feat(actions): add new security analysis action
   fix(linter): resolve ruff configuration issue
   docs(readme): update installation instructions
   test(pytest): add unit tests for builder module
   chore(deps): update dependencies to latest versions

   # Bad examples
   fix bug
   update stuff
   changes

Pull Request Process
--------------------

PR Title Format
~~~~~~~~~~~~~~~

**IMPORTANT**: PR titles must follow conventional commit format:

.. code-block:: text

   <type>[optional scope]: <description>

Examples:
- `feat(actions): add new security analysis action`
- `fix(linter): resolve ruff configuration issue`
- `docs(readme): update installation instructions`

PR Body Requirements
~~~~~~~~~~~~~~~~~~~~

**CRITICAL**: In the PR body, you MUST include the commit messages that will appear in the changelog. Each line must follow conventional commit format:

.. code-block:: markdown

   ## Changelog Entries

   The following commits will be included in the changelog:

   - feat(actions): add new security analysis action
   - fix(linter): resolve ruff configuration issue
   - docs(readme): update installation instructions
   - test(pytest): add unit tests for builder module

Support
=======

- **Issues**: `GitHub Issues <https://github.com/the-reacher-data/massive-devops/issues>`_
- **Discussions**: `GitHub Discussions <https://github.com/the-reacher-data/massive-devops/discussions>`_
- **Documentation**: `Project Wiki <https://github.com/the-reacher-data/massive-devops/wiki>`_

License
=======

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`_ file for details.

.. literalinclude:: ../LICENSE
   :language: text

---

**Made with ❤️ for the Python community**
