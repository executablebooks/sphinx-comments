"""Add a hypothes.is overlay to your Sphinx site."""

import os
from sphinx.util import logging

__version__ = "0.0.1"

logger = logging.getLogger(__name__)

def shp_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '_static'))
    app.config.html_static_path.append(static_path)

def activate_comments(app, pagename, templatename, context, doctree):
    """Activate commenting on each page."""
    kind = app.config.sphinx_comments.get("kind")
    # Load the hypothes.is script
    config = {"async": "async"}

    if kind in ["hypothes.is", "hypothesis"]:
        # If hypothesis, we just need to load the js library
        app.add_js_file("https://hypothes.is/embed.js", **config)
    elif kind in ["utterances"]:
        # Utterances needs the script placed where the comments will go.
        script = """
        <script src="https://utteranc.es/client.js"
            repo="executablebooks/sphinx-comments"
            issue-term="pathname"
            theme="github-light"
            crossorigin="anonymous"
            async>
        </script>
        """


def setup(app):
    logger.verbose('Adding copy buttons to code blocks...')
    # Add our static path
    app.connect('builder-inited', shp_static_path)
    app.connect('html-page-context', activate_comments)

    return {"version": __version__,
            "parallel_read_safe": True,
            "parallel_write_safe": True}
