import tkinter as tk


def builder(page, cid):
    info = page.components[cid]
    container = info["container"]
    config = info["config"]
    label_strvar = tk.StringVar()
    if config["title"]:
        label_strvar.set(config["title"])
    label = tk.Label(container,
                     textvariable=label_strvar)
    label.pack(anchor="w")
    show = None
    if config["secretive"]:
        show = "*"
    entry_strvar = tk.StringVar()
    if config["text"]:
        entry_strvar.set(config["text"])
    entry = tk.Entry(container, show=show,
                     textvariable=entry_strvar,
                     width=config["width"])
    entry.pack(anchor="w")
    on_submit = config["on_submit"]
    if on_submit:
        cache = (lambda e, page=page,
                        cid=cid,
                        on_submit=on_submit:
                            on_submit(page, cid))
        entry.bind("<Return>", cache)
    parts = {"label": label, "label_strvar": label_strvar,
             "entry": entry, "entry_strvar": entry_strvar}
    return parts


def reader(page, cid):
    cache = page.components[cid]
    parts = cache["parts"]
    config = cache["config"]
    return parts["entry_strvar"].get()


def updater(page, cid, **config):  # TODO
    info = page.components[cid]
    if "title" in config:
        title = config["title"]
        # update info
        info["config"]["title"] = title
        # update widget
        info["parts"]["label_strvar"].set(title)
    if "text" in config:
        text = config["text"]
        # update info
        info["config"]["text"] = text
        # update widget
        info["parts"]["entry_strvar"].set(text)
