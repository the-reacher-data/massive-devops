# Contributing to Massive DevOps

Thank you for your interest in contributing to Massive DevOps! This document provides guidelines and instructions for contributing to this project.

## 🚀 Quick Start

1. **Fork the repository**
2. **Create a feature branch** from `main`
3. **Make your changes** following our guidelines
4. **Create a Pull Request** with conventional commit format
5. **Wait for review** and merge approval

## 📋 Development Workflow

### Branch Protection

- **Main branch is protected**: Direct pushes to `main` are not allowed
- **Pull Requests required**: All changes must go through PRs
- **Squash merge only**: PRs are merged using squash merge to maintain clean history
- **Conventional Commits**: All commits must follow conventional commit format

### Branch Naming

Use descriptive branch names that indicate the type of change:

```bash
# Feature branches
feature/add-new-action
feature/improve-documentation

# Bug fixes
fix/linter-error-handling
fix/security-vulnerability

# Documentation
docs/update-readme
docs/add-examples

# Refactoring
refactor/cleanup-code
refactor/optimize-performance
```

## 📝 Commit Guidelines

### Conventional Commits Format

All commits must follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```text
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Supported Types

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

### Commit Examples

```bash
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
```

## 🔄 Pull Request Process

### PR Title Format

**IMPORTANT**: PR titles must follow conventional commit format:

```text
<type>[optional scope]: <description>
```

Examples:

- `feat(actions): add new security analysis action`
- `fix(linter): resolve ruff configuration issue`
- `docs(readme): update installation instructions`

### PR Body Requirements

**CRITICAL**: In the PR body, you MUST include the commit messages that will appear in the changelog. Each line must follow conventional commit format:

```markdown
## Changelog Entries

The following commits will be included in the changelog:

- feat(actions): add new security analysis action
- fix(linter): resolve ruff configuration issue
- docs(readme): update installation instructions
- test(pytest): add unit tests for builder module
```

### PR Template

Use this template for your PRs:

```markdown
## Description

Brief description of the changes made.

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Refactoring (no functional changes)
- [ ] Performance improvement
- [ ] Test addition or update

## Changelog Entries

The following commits will be included in the changelog:

- [conventional commit message 1]
- [conventional commit message 2]
- [conventional commit message 3]

## Testing

- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Existing tests updated if needed

## Checklist

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Conventional commit format used
- [ ] Changelog entries provided in PR body
```

## 🛠️ Development Setup

### Prerequisites

- Python 3.8+
- Git
- GitHub account

### Local Development

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/massive-devops.git
cd massive-devops

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/massive-devops.git

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run linting
ruff check .
mypy .
```

### Testing Your Changes

Before submitting a PR, ensure:

1. **Tests pass**: Run `pytest tests/`
2. **Linting passes**: Run `ruff check .`
3. **Type checking passes**: Run `mypy .`
4. **Security checks pass**: Run `bandit -r .`
5. **Documentation builds**: Run `sphinx-build docs/ docs/_build/html`

## 📚 Project Structure

```text
massive-devops/
├── actions/                 # GitHub Actions
│   ├── devops/             # DevOps-related actions
│   └── python/             # Python-specific actions
├── docs/                   # Documentation
├── tests/                  # Test files
├── workflows/              # Example workflows
├── pyproject.toml          # Project configuration
├── requirements-dev.txt     # Development dependencies
└── README.md               # Project documentation
```

## 🎯 Action Development Guidelines

### Creating New Actions

When creating new actions:

1. **Follow the structure**: Use the existing action structure as a template
2. **Include documentation**: Create a comprehensive README.md
3. **Add tests**: Include unit tests for your action
4. **Use conventional commits**: Follow the commit format
5. **Update main README**: Add your action to the main README table

### Action Structure

```bash
actions/
├── category/
│   └── action-name/
│       ├── action.yml          # Action definition
│       ├── README.md           # Documentation
│       ├── requirements.txt    # Dependencies
│       └── src/                # Source code
│           ├── cli.py          # Main script
│           └── templates/      # Jinja2 templates
│               └── report.md.j2
```

## 🔍 Code Review Process

### Review Criteria

PRs will be reviewed based on:

- **Code quality**: Clean, readable, and maintainable code
- **Functionality**: Works as expected and handles edge cases
- **Documentation**: Clear documentation and examples
- **Testing**: Adequate test coverage
- **Conventional commits**: Proper commit format
- **Changelog entries**: Correct changelog entries in PR body

### Review Process

1. **Automated checks**: CI/CD pipeline runs automatically
2. **Code review**: At least one maintainer reviews the PR
3. **Feedback**: Address any feedback or requested changes
4. **Approval**: PR is approved by maintainers
5. **Merge**: PR is squash-merged into main

## 🚨 Important Notes

### Changelog Generation

- **Automatic changelog**: The project uses conventional commits to generate changelogs
- **PR body requirement**: You MUST include changelog entries in your PR body
- **Conventional format**: Each changelog entry must follow conventional commit format
- **Squash merge**: PRs are squash-merged, so individual commits are preserved

### Python Focus

While many actions are focused on Python projects, the project welcomes contributions for:

- **Other languages**: Actions for JavaScript, Go, Rust, etc.
- **General DevOps**: Actions that work with any language
- **Infrastructure**: Actions for Docker, Kubernetes, etc.
- **Documentation**: Improvements to existing documentation

## 🤝 Community Guidelines

### Code of Conduct

- **Be respectful**: Treat everyone with respect and kindness
- **Be constructive**: Provide helpful feedback and suggestions
- **Be patient**: Remember that everyone is learning and contributing
- **Be inclusive**: Welcome contributors from all backgrounds

### Getting Help

- **GitHub Issues**: Use issues for bug reports and feature requests
- **GitHub Discussions**: Use discussions for questions and general discussion
- **Pull Requests**: Use PRs for code contributions

## 📞 Contact

- **Maintainers**: [List of maintainers]
- **Issues**: [GitHub Issues](https://github.com/your-org/massive-devops/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/massive-devops/discussions)

## 📄 License

By contributing to Massive DevOps, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

## Thank you for contributing to Massive DevOps! 🚀
