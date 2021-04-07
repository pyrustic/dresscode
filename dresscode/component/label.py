import tkinter as tk


def builder(page, cid):
    cache = page.components[cid]
    master = cache["master"]
    padding = cache["padding"]
    config = cache["config"]
    label = tk.Label(master, foreground=config["color"],
                     text=config["text"],
                     font=config["font"])
    label.pack(side=config["side"], anchor=config["anchor"],
               padx=padding[0], pady=padding[1])
    parts = {"label": label}
    return parts, data_getter


def data_getter(page, cid):
    return None
