# Security Comment

This GitHub Action runs Bandit security analysis on your Python code and posts a detailed security report as a PR comment. It helps identify potential security vulnerabilities and maintain secure coding practices.

## Features

- 🔒 **Bandit Integration**: Comprehensive Python security linter
- 🛡️ **Severity-based Filtering**: Configurable failure thresholds (none, low, medium, high)
- 📊 **Detailed Reports**: Shows specific security issues with file locations and descriptions
- 💬 **PR Comments**: Automatically posts/updates security reports in pull requests
- ⚙️ **Configurable Failure**: Choose when to fail the workflow based on severity
- 🎨 **Professional Reports**: Clean, collapsible markdown reports with Bandit branding

## Usage

### Basic Usage

```yaml
- name: Run Security Analysis
  uses: ./actions/python/security-comment
  with:
    src-dir: src
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

### Advanced Configuration

```yaml
- name: Run Security Analysis
  uses: ./actions/python/security-comment
  with:
    src-dir: lib
    github-token: ${{ secrets.GITHUB_TOKEN }}
    fail-on: medium  # Fail on medium or high severity issues
```

## Input Parameters

| Parameter | Description | Required | Default |
|-----------|-------------|----------|---------|
| `src-dir` | Source folder to scan | ❌ | `src` |
| `github-token` | GitHub token for posting PR comments | ✅ | - |
| `fail-on` | Severity threshold: `none`, `low`, `medium`, `high` | ❌ | `none` |

## Output Parameters

| Parameter | Description |
|-----------|-------------|
| `issues` | Number of Bandit security issues found |

## Severity Levels

### `fail-on: none` (Default)

The workflow will never fail due to security issues. All issues are reported but don't block the workflow.

### `fail-on: low`

The workflow will fail if any security issues are found (low, medium, or high severity).

### `fail-on: medium`

The workflow will fail only on medium or high severity issues.

### `fail-on: high`

The workflow will fail only on high severity issues.

## Bandit Configuration

Bandit is configured to run with the following settings:

- **Configuration**: Uses `pyproject.toml` for Bandit settings
- **Output format**: JSON for parsing
- **Source directory**: Configurable via `src-dir` parameter

### Common Security Checks

Bandit checks for various security issues including:

- **Hardcoded passwords**: Potential credential exposure
- **SQL injection**: Unsafe database queries
- **Command injection**: Unsafe subprocess calls
- **Path traversal**: Directory traversal vulnerabilities
- **Insecure randomness**: Weak random number generation
- **SSL/TLS issues**: Insecure cryptographic practices

## Workflow Integration

### Complete PR Workflow

```yaml
name: Security Analysis
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Security Analysis
        uses: ./actions/python/security-comment
        with:
          src-dir: src
          github-token: ${{ secrets.GITHUB_TOKEN }}
          fail-on: medium
```

### Non-blocking Security Check

```yaml
name: Security Analysis (Non-blocking)
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Security Analysis
        uses: ./actions/python/security-comment
        with:
          src-dir: src
          github-token: ${{ secrets.GITHUB_TOKEN }}
          fail-on: none  # Don't fail the workflow
```

## Report Format

The action generates a detailed markdown report with:

### Status Summary

- ✅ **Clean**: No security issues found
- ⚠️ **Issues Found**: Issues detected but below threshold
- ❌ **Blocking Issues**: Issues that will fail the workflow

### Security Details

- Issues count
- Detailed table with file, line, severity, confidence, test ID, and message
- Collapsible details for easy navigation

### Example Report

```markdown
# Bandit Security Report

**❌ Found 2 Bandit issues, including issues >= MEDIUM (blocking)**

---

<details>
<summary>🛡️ Bandit Findings (2)</summary>

| File | Line | Severity | Confidence | Test | Message |
|:-----|-----:|:--------:|:----------:|:-----|:--------|
| `src/auth.py` | 15 | HIGH | HIGH | B105 | Hardcoded password string |
| `src/db.py` | 23 | MEDIUM | HIGH | B608 | SQL injection possible |

</details>
```

## Dependencies

The action uses the following Python packages:

- `bandit~=1.7`: Python security linter
- `jinja2~=3.1`: Template engine for report generation
- `tomlkit~=0.13`: TOML configuration parser
- `markupsafe~=2.1`: Safe string handling

## Configuration

### Bandit Configuration in pyproject.toml

```toml
[tool.bandit]
exclude_dirs = ["tests", "migrations"]
skips = ["B101", "B601"]  # Skip specific tests

[tool.bandit.assert_used]
skips = ["*_test.py", "test_*.py"]
```

### Custom Template

You can use a custom Jinja2 template for the report:

```yaml
- name: Run Security Analysis
  uses: ./actions/python/security-comment
  with:
    src-dir: src
    github-token: ${{ secrets.GITHUB_TOKEN }}
    template: ./custom-security-template.md.j2
```

### Template Variables

The template has access to these variables:

- `issues`: List of BanditIssue objects
- `count`: Number of issues found
- `status_msg`: Status message with emoji

## Directory Structure

```text
project/
├── src/                    # Source code (scanned by default)
│   ├── auth.py
│   ├── db.py
│   └── api.py
├── tests/                  # Excluded by default
├── migrations/            # Excluded by default
└── pyproject.toml         # Bandit configuration
```

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure your source code is properly structured
2. **Permission errors**: Verify GitHub token has comment permissions
3. **Bandit not found**: Check that dependencies are installed correctly
4. **Configuration errors**: Verify Bandit configuration in pyproject.toml

### Debug Mode

To debug the security analysis, you can run Bandit manually:

```bash
# Run Bandit with JSON output
bandit -c pyproject.toml -r src -f json -o bandit.json

# Run Bandit with text output for debugging
bandit -c pyproject.toml -r src
```

### Security Best Practices

1. **Start with `fail-on: none`** for gradual adoption
2. **Review security reports** regularly to improve code security
3. **Configure Bandit** with project-specific exclusions
4. **Address high severity issues** immediately
5. **Use security-focused code reviews** for sensitive modules

## License

This project is licensed under the same license as the main repository.
