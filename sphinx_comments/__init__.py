"""Add a hypothes.is overlay to your Sphinx site."""

import os
from docutils import nodes
from sphinx.util import logging

__version__ = "0.0.1"

logger = logging.getLogger(__name__)

def shp_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '_static'))
    app.config.html_static_path.append(static_path)

def activate_comments(app, pagename, templatename, context, doctree):
    """Activate commenting on each page."""
    config = app.config.comments_config
    if not isinstance(config, (dict, type(None))):
        raise ValueError("Comments configuration must be a dictionary.")

    extra_config = {"async": "async"}
    if config.get("hypothesis"):
        # If hypothesis, we just need to load the js library
        app.add_js_file("https://hypothes.is/embed.js", **extra_config)

    if config.get("utterances"):
        dom = """
            const runWhenDOMLoaded = cb => {
            if (document.readyState != 'loading') {
                cb()
            } else if (document.addEventListener) {
                document.addEventListener('DOMContentLoaded', cb)
            } else {
                document.attachEvent('onreadystatechange', function() {
                if (document.readyState == 'complete') cb()
                })
            }
            }
        """
        if doctree:
            js = f"""
            {dom}
            var addUtterances = () => {{
                section = document.querySelectorAll("div.section")[1]
                var script = document.createElement("script");
                script.type = "text/javascript";
                script.src = "https://utteranc.es/client.js";
                script.async = "async";

                script.setAttribute("repo", "executablebooks/sphinx-comments");
                script.setAttribute("issue-term", "pathname");
                script.setAttribute("theme", "github-light");
                script.setAttribute("label", "💬 comment");
                script.setAttribute("crossorigin", "anonymous");
                section.appendChild(script);
            }}
            runWhenDOMLoaded(addUtterances)

            """
            app.add_js_file(None, body=js)


class UtterancesScriptNode(nodes.Element):
    """Appends the Utterances script to the output HTML.
    """

    def __init__(self, rawsource="", repo=None, *children, **attributes):
        super().__init__("", repo=repo)

    def html(self):

        return script

    def depart_html(self):
        return "</script>"


def setup(app):
    app.add_config_value("comments_config", {}, "html")

    # Add our static path
    app.connect('builder-inited', shp_static_path)
    app.connect('html-page-context', activate_comments)

    return {"version": __version__,
            "parallel_read_safe": True,
            "parallel_write_safe": True}
