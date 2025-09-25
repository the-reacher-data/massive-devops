# Pytest Comment

This GitHub Action runs pytest with coverage analysis and posts a comprehensive test report as a PR comment. It provides detailed test results, coverage metrics, and helps maintain code quality through automated testing.

## Features

- 🧪 **Pytest Integration**: Run tests with comprehensive reporting
- 📊 **Coverage Analysis**: Track code coverage with configurable thresholds
- 📈 **Visual Reports**: Beautiful markdown reports with badges and tables
- 💬 **PR Comments**: Automatically posts/updates test reports in pull requests
- 🔍 **Detailed Analysis**: Shows failed tests and files below coverage threshold
- 📤 **Codecov Integration**: Optional upload to Codecov for coverage tracking
- ⚙️ **Configurable Thresholds**: Set minimum coverage requirements

## Usage

### Basic Usage

```yaml
- name: Run Tests with Coverage
  uses: ./actions/python/pytest-comment
  with:
    test-dir: tests
    src-dir: src
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

### Advanced Configuration

```yaml
- name: Run Tests with Coverage
  uses: ./actions/python/pytest-comment
  with:
    test-dir: src/tests
    src-dir: src
    coverage-threshold: 90
    github-token: ${{ secrets.GITHUB_TOKEN }}
    codecov-token: ${{ secrets.CODECOV_TOKEN }}
```

## Input Parameters

| Parameter | Description | Required | Default |
|-----------|-------------|----------|---------|
| `test-dir` | Directory with tests | ❌ | `src/tests` |
| `src-dir` | Source folder measured by coverage | ❌ | `src` |
| `coverage-threshold` | Minimum coverage percentage | ❌ | `85` |
| `github-token` | GitHub token for posting PR comments | ✅ | - |
| `codecov-token` | Codecov token for coverage upload | ❌ | - |

## Output Parameters

| Parameter | Description |
|-----------|-------------|
| `coverage` | Global coverage percentage |
| `failed` | Number of failed tests |

## Coverage Thresholds

The action uses coverage thresholds to determine if the code quality meets requirements:

- **Default**: 85% coverage threshold
- **Configurable**: Set any percentage (0-100)
- **Failure**: Workflow fails if coverage is below threshold
- **Reporting**: Files below threshold are highlighted in the report

## Pytest Configuration

Pytest is configured to run with the following settings:

- **Coverage reporting**: JSON, XML, and terminal output
- **JUnit XML**: For test result parsing
- **Verbose output**: Detailed test execution information
- **Short traceback**: Concise error reporting

### Coverage Reports Generated

- `coverage.json`: Detailed coverage data for parsing
- `coverage.xml`: XML format for external tools
- `junit.xml`: Test results in JUnit format

## Workflow Integration

### Complete PR Workflow

```yaml
name: Test Suite
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Tests with Coverage
        uses: ./actions/python/pytest-comment
        with:
          test-dir: tests
          src-dir: src
          coverage-threshold: 85
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

### With Codecov Integration

```yaml
name: Test Suite with Codecov
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Tests with Coverage
        uses: ./actions/python/pytest-comment
        with:
          test-dir: tests
          src-dir: src
          coverage-threshold: 85
          github-token: ${{ secrets.GITHUB_TOKEN }}
          codecov-token: ${{ secrets.CODECOV_TOKEN }}
```

## Report Format

The action generates a comprehensive markdown report with:

### Summary Section

- ✅ **Passed tests**: Number of successful tests
- ❌ **Failed tests**: Number of failed tests
- ⏭ **Skipped tests**: Number of skipped tests
- 🧪 **Total tests**: Total number of tests executed
- 📈 **Coverage**: Coverage percentage with color-coded badge

### Details Section

- **Failed Tests**: Detailed table with test names and error messages
- **Coverage Issues**: Files below the coverage threshold

### Example Report

```markdown
# Pytest Report

## 📊 Summary

| Metric          | Value |
|-----------------|-------|
| ✅ Passed tests | **45** |
| ❌ Failed tests | **2** |
| ⏭ Skipped tests | **1** |
| 🧪 Total tests  | **48** |
| 📈 Coverage     | ![coverage](https://img.shields.io/badge/87%25-green?style=for-the-badge&logo=pytest) |

❌ Some tests failed. Please review the details below.

---

## 🔍 Details

<details>
<summary>❌ Failed Tests (2)</summary>

| Test | Message |
|------|---------|
| `test_auth.py::test_login_failure` | AssertionError: Expected status 401, got 200 |
| `test_api.py::test_create_user` | ValidationError: Invalid email format |

</details>

<details>
<summary>⚠️ Files Below Coverage Threshold (85%)</summary>

| File | Coverage |
|------|----------|
| `src/utils.py` | 78% |
| `src/legacy.py` | 65% |

</details>
```

## Dependencies

The action uses the following Python packages:

- `pytest~=8.3`: Testing framework
- `pytest-cov~=5.0`: Coverage plugin for pytest
- `pytest-asyncio~=0.23`: Async support for pytest
- `coverage[toml]~=7.6`: Coverage measurement
- `jinja2~=3.1`: Template engine for report generation

## Configuration

### Pytest Configuration in pyproject.toml

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"

[tool.coverage.run]
source = ["src"]
omit = ["tests/*", "migrations/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
]
```

### Coverage Configuration

```toml
[tool.coverage.run]
source = ["src"]
omit = [
    "tests/*",
    "migrations/*",
    "*/venv/*",
    "*/env/*",
]

[tool.coverage.report]
precision = 2
show_missing = true
skip_covered = false
```

## Directory Structure

```bash
project/
├── src/                    # Source code (measured for coverage)
│   ├── main.py
│   ├── utils.py
│   └── api.py
├── tests/                  # Test directory
│   ├── test_main.py
│   ├── test_utils.py
│   └── test_api.py
└── pyproject.toml          # Pytest and coverage configuration
```

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure test directory structure is correct
2. **Coverage issues**: Check source directory configuration
3. **Permission errors**: Verify GitHub token has comment permissions
4. **Test failures**: Review test output and fix failing tests

### Debug Mode

To debug the testing process, you can run pytest manually:

```bash
# Run tests with coverage
pytest tests/ --cov=src --cov-report=term-missing --cov-report=json:coverage.json

# Run specific test file
pytest tests/test_main.py -v

# Run with detailed output
pytest tests/ -v --tb=long
```

### Test Best Practices

1. **Write comprehensive tests** for all critical functionality
2. **Maintain high coverage** but focus on meaningful tests
3. **Use descriptive test names** that explain what is being tested
4. **Mock external dependencies** to ensure test isolation
5. **Review test reports** regularly to improve test quality

## Codecov Integration

### Setup Codecov

1. **Sign up** at [codecov.io](https://codecov.io)
2. **Add repository** to Codecov
3. **Get token** from Codecov dashboard
4. **Add secret** `CODECOV_TOKEN` to GitHub repository

### Benefits

- **Historical tracking**: Coverage trends over time
- **PR comments**: Coverage changes in pull requests
- **Badges**: Coverage badges for README
- **Advanced reporting**: Detailed coverage analysis

## License

This project is licensed under the same license as the main repository.
