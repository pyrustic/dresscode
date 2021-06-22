import tkinter as tk
from megawidget.pathentry import Pathentry


def builder(page, cid):
    info = page.components[cid]
    container = info["container"]
    padding = info["padding"]
    config = info["config"]
    # title
    label = tk.Label(container, text=config["title"])
    label.pack(anchor="w")
    # items container
    pathentry = Pathentry(container, browse=config["browse"],
                          width=config["width"])
    pathentry.pack(anchor="w")
    str_var = pathentry.string_var
    on_submit = config["on_submit"]
    if config["text"]:
        str_var.set(config["text"])
    if on_submit:
        cache = (lambda e, page=page,
                        cid=cid,
                        on_submit=on_submit:
                 on_submit(page, cid))
        pathentry.components["entry"].bind("<Return>", cache)
    parts = {"pathentry": pathentry, "str_var": str_var,
             "label": label}
    return parts


def reader(page, cid):
    cache = page.components[cid]
    parts = cache["parts"]
    config = cache["config"]
    return parts["str_var"].get()


def updater(page, cid, **config):  # TODO
    pass
