# Hypothesis

test

```{raw} html
<script async="async" src="https://hypothes.is/embed.js"></script>
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