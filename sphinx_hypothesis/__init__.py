"""Add a hypothes.is overlay to your Sphinx site."""

import os
from sphinx.util import logging

__version__ = "0.0.1"

logger = logging.getLogger(__name__)

def shp_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '_static'))
    app.config.html_static_path.append(static_path)

def add_to_context(app, config):
    # Update the global context
    config.html_context.update({'copybutton_prompt_text': config.copybutton_prompt_text})
    config.html_context.update({'copybutton_only_copy_prompt_lines': config.copybutton_only_copy_prompt_lines})
    config.html_context.update({'copybutton_remove_prompts': config.copybutton_remove_prompts})
    config.html_context.update({'copybutton_image_path': config.copybutton_image_path})
    config.html_context.update({'copybutton_selector': config.copybutton_selector})

def setup(app):
    logger.verbose('Adding copy buttons to code blocks...')
    # Add our static path
    app.connect('builder-inited', shp_static_path)

    # Load the hypothes.is script
    config = {"async": "async"}
    app.add_js_file("https://hypothes.is/embed.js", **config)

    return {"version": __version__,
            "parallel_read_safe": True,
            "parallel_write_safe": True}
