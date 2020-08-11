# Sphinx Comments

[![PyPI](https://img.shields.io/pypi/v/sphinx-comments.svg)](https://pypi.org/project/sphinx_comments/) | [![Documentation](https://readthedocs.org/projects/sphinx-comments/badge/?version=latest)](https://sphinx-comments.readthedocs.io/en/latest/?badge=latest)

Add comments and annotation functionality to your Sphinx website.

Currently, these commenting engines are supported:

- [Hypothes.is](https://hypothes.is/) provides a web overlay that allows you to annotate and comment collaboratively.
- [utteranc.es](https://utteranc.es/) is a web commenting system that uses GitHub Issues to store and manage comments.
- [`dokie.li`](https://dokie.li/) is an open source commenting and annotation overlay built on web standards.

For examples of each service, as well as instructions for how to activate it,
[see the `sphinx-comments` documentation](https://sphinx-comments.readthedocs.io/en/latest).

## Contribute to Sphinx Comments

Sphinx Comments follows [the Executable Books contributing guide](https://github.com/executablebooks/.github/blob/master/CONTRIBUTING.md).

### Install for development

To install `sphinx-comments` for development, take the following steps:

```bash
git clone https://github.com/executablebooks/sphinx-comments
cd sphinx-comments
pip install -e .[testing,sphinx]
```

This will install the dependencies needed for development and testing.

### Repository structure

Sphinx Comments is a lightweight Sphinx extension that activates several Javascript libraries for use within Sphinx. All of its functionality is contained in `sphinx_comments/__init__.py`.

As a general rule, Sphinx Comments tries to be as lightweight as possible. It simply:

- Loads Javscript libraries for web commenting and annotation platforms
- Provides a configuration layer for platforms that support it

Note that some of these platforms cannot be activated at the same time, users
will need to choose one or the other.

Some of the annotation platforms require more complex setup - for example, `utteranc.es` requires its script to be placed in a specific location on the page, and so `sphinx-comments` will place it directly in the doctree of the page (underneath the content).
