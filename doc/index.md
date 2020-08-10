# Sphinx Comments

Add comments and annotation functionality to your Sphinx website.

Currently, these commenting engines are supported:

- [Hypothes.is](https://hypothes.is/) provides a web overlay that allows you to annotate and comment collaboratively.
- [utteranc.es](https://utteranc.es/) is a web commenting system that uses GitHub Issues to store and manage comments.
- [`dokie.li`](https://dokie.li/) is an open source commenting and annotation overlay built on web standards.

For examples of each service, as well as instructions for how to activate it,
click on the links to the left.

## Installation

Clone and install the github reposiory

```bash
pip install git+https://github.com/choldgraf/sphinx-comments
```

Next, activate the extension by adding it to your `conf.py` file:

```python
...
html_extensions = [
   "sphinx_comments"
]
```

## Configuration

To configure `sphinx-comments` (and to choose the engine you'd like to use),
you should configure the `comments_config` dictionary in `conf.py`. Instructions
for doing so can be found in the page for each of the supported engines below.

```{toctree}
:caption: Supported engines
:maxdepth: 2
hypothesis
dokieli
utterances
```
