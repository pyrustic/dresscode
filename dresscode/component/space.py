import tkinter as tk


def builder(page, cid):
    cache = page.components[cid]
    master = cache["master"]
    padding = cache["padding"]
    config = cache["config"]
    frame = tk.Frame(master, width=config["width"],
                     height=config["height"])
    frame.pack(side=config["side"], anchor=config["anchor"],
               padx=padding[0], pady=padding[1])
    parts = {"frame": frame}
    return parts, data_getter


def data_getter(page, cid):
    return None
