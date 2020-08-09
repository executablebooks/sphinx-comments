# Sphinx Hypothes.is

Add a [hypothes.is overlay](https://web.hypothes.is/) to your documentation.
This extension simply activates the hypothes.is javascript bundle on your
Sphinx site. This will cause the hypothes.is overlay to be shown, allowing your
readers to log-in and comment on your documentation if they have questions.

## Installation

Clone and install the github reposiory

```bash
git clone https://github.com/choldgraf/sphinx-comments
cd sphinx-comments
pip install -e .
```

Next, activate the extension by adding it to your `conf.py` file:

```python
...
html_extensions = [
   "sphinx_comments"
]
```

When you build your documentation, you will see the hypothes.is overlay to the
right of your screen.
