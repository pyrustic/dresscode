import tkinter as tk


def builder(page, cid):
    info = page.components[cid]
    container = info["container"]
    padding = info["padding"]
    config = info["config"]
    frame = tk.Frame(container, width=config["width"],
                     height=config["height"])
    frame.pack(side=config["side"], anchor=config["anchor"],
               padx=padding[0], pady=padding[1])
    parts = {"frame": frame}
    return parts


def reader(page, cid):
    return None


def updater(page, cid, **config):  # TODO
    pass
