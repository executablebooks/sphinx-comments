# Dokieli

```{raw} html
<script src="https://dokie.li/scripts/dokieli.js"></script>
<link media="all" rel="stylesheet" type="text/css" href="https://dokie.li/media/css/dokieli.css" />
```

```{warning}
Dokieli is experimental and may not behave as expected right now!
```

[`dokie.li`](https://dokie.li/) is a clientside editor for decentralised article publishing, annotations and social interactions. Dokieli is activated on this page. You can see the web overlay by clicking on the hamburger menu in the upper-right corner of this page.

## Activate `dokie.li`

You can activate [`dokie.li`](https://dokie.li/)
by adding the following to your `conf.py` file:

```python
comments_config = {
   "dokieli": True
}
```

Next, [follow the `dokie.li` configuration instructions](https://dokie.li/).

When you build your documentation, pages will now have an active dokieli overlay.
