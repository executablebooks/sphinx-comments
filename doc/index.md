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

## Activate `hypothes.is`

You can activate `hypothes.is` by adding the following to your `conf.py` file:

```python
comments_config = {
   "hypothesis": True
}
```

This will add a [hypothes.is overlay](https://web.hypothes.is/) to your documentation. This extension simply activates the hypothes.is javascript bundle on your Sphinx site. This will cause the hypothes.is overlay to be shown, allowing your readers to log-in and comment on your documentation if they have questions.

When you build your documentation, you will see the hypothes.is overlay to the right of your screen.

## Activate `utteranc.es`

You can activate `utteranc.es` by adding the following to your `conf.py` file:

```python
comments_config = {
   "utterances": True
}
```

Next, [follow the `utteranc.es` configuration instructions](https://utteranc.es/#configuration).

When you build your documentation, pages will now have a comment box at the bottom. If readers log in via GitHub they will be able to post comments that will then map onto issues in your GitHub repository.
