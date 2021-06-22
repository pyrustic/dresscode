import tkinter as tk


def builder(page, cid):
    info = page.components[cid]
    container = info["container"]
    padding = info["padding"]
    config = info["config"]
    label = tk.Label(container, foreground=config["color"],
                     text=config["text"],
                     font=config["font"])
    label.pack(side=config["side"], anchor=config["anchor"],
               padx=padding[0], pady=padding[1])
    parts = {"label": label}
    return parts


def reader(page, cid):
    return None


def updater(page, cid, **config):  # TODO
    pass
