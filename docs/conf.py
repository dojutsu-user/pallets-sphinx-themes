from pallets_sphinx_themes import get_version
from pallets_sphinx_themes import ProjectLink

# Project --------------------------------------------------------------

project = "Pallets Sphinx Themes"
copyright = "2007 Pallets"
author = "Pallets"
release, version = get_version("Pallets-Sphinx-Themes")

# General --------------------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "pallets_sphinx_themes",
    "sphinxcontrib.log_cabinet",
    "sphinx_issues",
]
issues_github_path = "pallets/pallets-sphinx-themes"

# HTML -----------------------------------------------------------------

html_theme = "flask"
html_context = {
    "project_links": [
        ProjectLink("Donate to Pallets", "https://palletsprojects.com/donate"),
        ProjectLink("Pallets Website", "https://palletsprojects.com/"),
        ProjectLink("PyPI releases", "https://pypi.org/project/Pallets-Sphinx-Themes/"),
        ProjectLink("Source Code", "https://github.com/pallets/pallets-sphinx-themes/"),
        ProjectLink(
            "Issue Tracker", "https://github.com/pallets/pallets-sphinx-themes/issues/"
        ),
    ]
}
html_sidebars = {
    "index": ["project.html", "localtoc.html", "searchbox.html"],
    "**": ["localtoc.html", "relations.html", "searchbox.html"],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html"]}
html_title = "{} Documentation ({})".format(project, version)
html_show_sourcelink = False
