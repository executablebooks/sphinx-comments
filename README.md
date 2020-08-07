# sphinx-hypothesis

[![PyPI](https://img.shields.io/pypi/v/sphinx-hypothesis.svg)](https://pypi.org/project/sphinx_hypothesis/) | [![Documentation](https://readthedocs.org/projects/sphinx-hypothesis/badge/?version=latest)](https://sphinx-hypothesis.readthedocs.io/en/latest/?badge=latest)

A small sphinx extension to add a "copy" button to code blocks.

See [the sphinx-hypothesis documentation](https://sphinx-hypothesis.readthedocs.io/en/latest/) for more details!

![](doc/_static/copybutton.gif)

## Installation

You can install `sphinx-hypothesis` with `pip`:

```
pip install sphinx-hypothesis
```

## Usage

In your `conf.py` configuration file, add `sphinx_hypothesis` to your extensions list.
E.g.:

```
extensions = [
    ...
    'sphinx_hypothesis'
    ...
]
```

When you build your site, your code blocks should now have little copy buttons to their
right. Clicking the button will copy the code inside!

## Customization

If you'd like to customize the look of the copy buttons, you can over-write any of the
CSS rules specified in the sphinx-hypothesis CSS file ([link](sphinx_hypothesis/_static/copybutton.css))
