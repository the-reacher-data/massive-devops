from __future__ import annotations

import os
import shutil
import tomllib
from datetime import datetime
from pathlib import Path

from sphinx.util import logging

logger = logging.getLogger(__name__)


# --- Read pyproject.toml ---
pyproject = Path(__file__).parent.parent / "pyproject.toml"
with pyproject.open("rb") as f:
    data = tomllib.load(f)

proj = data.get("project", {})

# --- Project info ---
project = proj.get("name", "Unknown Project")
author = ", ".join(a.get("name", "") for a in proj.get("authors", []))
copyright = f"{datetime.now().year}, {author}"
release = proj.get("version", "0.0.0")

# --- Extensions ---
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

html_theme = "furo"

autodoc_typehints = "description"
add_module_names = False


def on_build_finished(app, exception):
    build_static = Path(app.outdir) / "_static"
    if Path(build_static).exists():
        for root, _dirs, files in os.walk(build_static):
            for name in files:
                path = Path(root) / name
                if path.is_symlink():
                    target = path.readlink()
                    path.unlink()
                    shutil.copy(target, path)
                    logger.info(f"Replaced symlink {path} with copy")


def setup(app):
    app.connect("build-finished", on_build_finished)
