# Changelog Conventional Commit

This GitHub Action automatically generates changelogs from conventional commits, supporting both PR preview mode and release mode with squash commits.

## Features

- 🎯 **Two operation modes**: PR preview and release
- 📝 **Full Conventional Commits support**: feat, fix, docs, style, refactor, perf, test, chore
- 🏷️ **Grouping by type and scope**: Automatically organizes commits by category
- 🔗 **Commit links**: Includes SHA references and direct GitHub links
- 🎨 **Customizable template**: Uses Jinja2 to generate output format
- �� **PR preview**: Automatically updates PR comments with changelog

## Usage

### PR Mode (Preview)

Generate a changelog preview for a pull request:

```yaml
- name: Generate PR Changelog Preview
  uses: ./actions/devops/changelog-conventional-commit
  with:
    mode: pr
    branch: ${{ github.head_ref }}
    version: UNRELEASED
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

### Release Mode

Generate a changelog for a release using the squash commit:

```yaml
- name: Generate Release Changelog
  uses: ./actions/devops/changelog-conventional-commit
  with:
    mode: release
    branch: main
    version: v1.2.3
    pr-number: 123
```

## Input Parameters

| Parameter | Description | Required | Default |
|-----------|-------------|----------|---------|
| `mode` | Operation mode: `pr` or `release` | ✅ | - |
| `branch` | Branch name | ✅ | - |
| `version` | Release version (optional) | ❌ | - |
| `template` | Path to custom Jinja2 template | ❌ | Default template |
| `pr-number` | PR number of the squash commit | ❌ | - |
| `output` | Output Markdown file | ❌ | `changelog_preview.md` |
| `github-token` | GitHub token (only needed in PR mode) | ❌ | - |

## Output Parameters

| Parameter | Description |
|-----------|-------------|
| `changelog_b64` | Generated changelog in Markdown format (base64-encoded) |
| `output_path` | Path to the generated Markdown file |

## Conventional Commits Format

The action follows the [Conventional Commits](https://www.conventionalcommits.org/) specification to parse and categorize commits. The format is:

### Supported Types

- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `style`: Formatting changes (spaces, commas, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or modifying tests
- `chore`: Maintenance tasks
- `other`: Other changes (commits that don't follow the format)

### Commit Examples

```bash
feat(auth): add OAuth2 authentication
fix(api): fix 500 error in /users endpoint
docs(readme): update installation instructions
style(lint): fix formatting issues with black
refactor(db): optimize database queries
perf(cache): implement Redis caching
test(unit): add validation module tests
chore(deps): update security dependencies
```

## Custom Template

You can use your own custom Jinja2 template:

```yaml
- name: Generate Changelog with Custom Template
  uses: ./actions/devops/changelog-conventional-commit
  with:
    mode: pr
    branch: feature-branch
    template: ./custom-template.md.j2
```

### Available Template Variables

- `version`: Release version
- `commits`: Dictionary of commits grouped by type and scope
- `repo_url`: Repository URL
- `squash`: Squash commit information (only in release mode)
- `is_unreleased`: Boolean indicating if it's an unreleased version
- `pr_number`: PR number (only in release mode)

## Output Examples

### PR Mode

```markdown
# ✨ Changelog preview for feature-branch (UNRELEASED)

## ✨ Features
### auth
- **oauth:** add Google OAuth2 support ([`a1b2c3d`](https://github.com/user/repo/commit/a1b2c3d))

### api
- **users:** implement user creation endpoint ([`e4f5g6h`](https://github.com/user/repo/commit/e4f5g6h))

## �� Fixes
### database
- **connection:** fix database connection timeout ([`i7j8k9l`](https://github.com/user/repo/commit/i7j8k9l))
```

### Release Mode

```markdown
# 🚀 Release v1.2.3 ([#123](https://github.com/user/repo/pull/123)) ([`a1b2c3d`](https://github.com/user/repo/commit/a1b2c3d))

## ✨ Features
### auth
- **oauth:** add Google OAuth2 support

## 🐛 Fixes
### database
- **connection:** fix database connection timeout
```

## Workflow Integration

### Complete PR Workflow

```yaml
name: PR Changelog Preview
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Generate Changelog Preview
        uses: ./actions/devops/changelog-conventional-commit
        with:
          mode: pr
          branch: ${{ github.head_ref }}
          version: UNRELEASED
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

### Complete Release Workflow

```yaml
name: Release Changelog
on:
  push:
    tags:
      - 'v*'

jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Generate Release Changelog
        uses: ./actions/devops/changelog-conventional-commit
        with:
          mode: release
          branch: main
          version: ${{ github.ref_name }}
          pr-number: ${{ github.event.number }}
```

## Dependencies

- Python 3.8+
- Jinja2 ~3.1

## Important Notes

- In PR mode, the action automatically compares with `origin/main`
- Commits starting with `WIP:` are ignored
- In release mode, the current commit is expected to be a squash commit
- The action automatically updates PR comments when used in PR mode
- Commits that don't follow the conventional format are grouped under "Other"

## License

This project is licensed under the same license as the main repository.
