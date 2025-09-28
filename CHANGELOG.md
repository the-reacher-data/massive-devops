# 🚀 Release 0.1.0 ([#15](https://github.com/the-reacher-data/massive-devops/pull/15)) ([`47f36b2`](https://github.com/the-reacher-data/massive-devops/commit/47f36b2b72d56f7e0c7e8763d5af355e7cc5901f))


## ✨ Features
### devops
- **devops:** add semantic versioning and changelog actions<br>
  > Implemented `versioning-branch-semantic` action with support for prereleases and release rules from pyproject.toml
  > Added `changelog-conventional-commit` action to autogenerate changelogs in PRs and squash merges
  > Integrated PR comments with hidden tags to track source branches


### python
- **python:** introduce reusable composite actions<br>
  > Added `uv-requirements` for lightweight dependency management
  > Added `linter-comment` action running Ruff and MyPy with configurable excludes
  > Added `pytest-comment` action with coverage thresholds
  > Added `security-comment` action wrapping Bandit with severity threshold


### docs
- **docs:** add Sphinx-based documentation generator<br>
  > Autogenerate API docs with `sphinx-apidoc`
  > Support both GitHub Pages (release) and artifact previews (PRs)
  > Integrated `myst-parser` to include Markdown files and README.md
  > Added Furo theme and improved UX for enterprise-style output



## 🐛 Fixes
### ci
- **ci:** correct GitHub Actions output handling<br>
  > Fixed multiline outputs by wrapping them with EOF delimiters
  > Corrected incorrect input names (config-file vs pyproject.toml)
  > Fixed PR comment updates not replacing previous outputs


### changelog
- **changelog:** handle squash commit bodies correctly<br>
  > Support lines starting with `*`, `**`, or direct conventional commit patterns
  > Treat lines starting with `-` as continuation of previous commit body
  > Added robust parsing for multi-line descriptions



## 📖 Documentation
### (no scope)
- update READMEs for all actions<br>
  > Each composite action now has a dedicated README with usage examples
  > Added badges for PyPI, Python versions, and GitHub Actions status
  > Documented end-to-end DevOps workflow with examples for PRs and releases




## ♻️ Refactor
### workflows
- **workflows:** split CI and Release workflows<br>
  > CI workflow (`python-ci.yml`) parametrized for lint, test, security, and prerelease publish
  > Release workflow (`python-release.yml`) retrieves PR source branch, runs versioning and changelog, and conditionally publishes
  > Added concurrency to prevent reruns from clashing
  > Improved structure with jobs: detect-branch, versioning, changelog, publish, tag, docs, codeql





## 🛠 Chores
### (no scope)
- configure repo rules and branch protections<br>
  > Enforced squash merges only on main
  > Added PR review requirements and bypass options for automation
  > Added pre-commit hooks with Ruff, Black, and isort for local dev consistency





# 🚀 Release 0.0.2 ([#13](https://github.com/the-reacher-data/massive-devops/pull/13)) ([`a0b5b81`](https://github.com/the-reacher-data/massive-devops/commit/a0b5b8121490b32fc8bcff86341a6ad418724612))












# 🚀 Release 0.1.0 ([#5](https://github.com/the-reacher-data/massive-devops/pull/5)) ([`efe70b9`](https://github.com/the-reacher-data/massive-devops/commit/efe70b96d686655c6bb03b4de2ff71e0d8b98d8f))
