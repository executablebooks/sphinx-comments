# sphinx-comments

[![PyPI](https://img.shields.io/pypi/v/sphinx-comments.svg)](https://pypi.org/project/sphinx_comments/) | [![Documentation](https://readthedocs.org/projects/sphinx-comments/badge/?version=latest)](https://sphinx-comments.readthedocs.io/en/latest/?badge=latest)

A small sphinx extension to add a "copy" button to code blocks.

See [the sphinx-comments documentation](https://sphinx-comments.readthedocs.io/en/latest/) for more details!

![](doc/_static/copybutton.gif)

## Installation

You can install `sphinx-comments` with `pip`:

```
pip install sphinx-comments
```

## Usage

In your `conf.py` configuration file, add `sphinx_comments` to your extensions list.
E.g.:

```
extensions = [
    ...
    'sphinx_comments'
    ...
]
```

When you build your site, your code blocks should now have little copy buttons to their
right. Clicking the button will copy the code inside!

## Customization

If you'd like to customize the look of the copy buttons, you can over-write any of the
CSS rules specified in the sphinx-comments CSS file ([link](sphinx_comments/_static/copybutton.css))
