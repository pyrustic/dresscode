import tkinter as tk
from pyrustic.widget.pathentry import Pathentry


def builder(page, cid):
    cache = page.components[cid]
    master = cache["master"]
    padding = cache["padding"]
    config = cache["config"]
    # container
    frame = tk.Frame(master)
    frame.pack(side=config["side"], anchor=config["anchor"],
               padx=padding[0], pady=padding[1])
    # title
    label = tk.Label(frame, text=config["title"])
    label.pack(anchor="w")
    # items container
    pathentry = Pathentry(frame, width=config["width"])
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
             "label": label, "frame": frame}
    return parts, data_getter


def data_getter(page, cid):
    cache = page.components[cid]
    parts = cache["parts"]
    config = cache["config"]
    return parts["str_var"].get()
