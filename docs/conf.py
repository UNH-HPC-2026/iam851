# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'IAM 851 class notes'
copyright = '2026, Kai Germaschewski'
author = 'Kai Germaschewski'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    # "nbsphinx",
    "sphinx.ext.autodoc",
    # "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinxcontrib.mermaid",
    # "sphinx_autodoc_typehints",
    # "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ['_static']

source_suffix = [".rst", ".md"]

html_title = ""

html_logo = "unhhpc.png"

html_theme_options = dict(  # noqa: C408
    repository_url="https://github.com/UNH-HPC-2026/iam851",
    repository_branch="main",
    navigation_with_keys=False,  # pydata/pydata-sphinx-theme#1492
    navigation_depth=4,
    path_to_docs="docs",
    use_edit_page_button=True,
    use_repository_button=True,
    use_issues_button=True,
    home_page_in_toc=False,
)

todo_include_todos = True



