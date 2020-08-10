# Sphinx Comments

Add comments and annotation functionality to your Sphinx website.

Currently, two commenting engines are supported:

- [Hypothes.is](https://hypothes.is/) provides a web overlay that allows you to annotate and comment collaboratively.
- [utteranc.es](https://utteranc.es/) is a web commenting system that uses GitHub Issues to store and manage comments.

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

```{toctree}
hypothesis
dokieli
utterances
```
