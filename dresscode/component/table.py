import tkinter as tk
from megawidget.table import Table


def builder(page, cid):
    info = page.components[cid]
    container = info["container"]
    padding = info["padding"]
    config = info["config"]
    frame = tk.Frame(container)
    frame.pack(side=config["side"], anchor=config["anchor"],
               padx=padding[0], pady=padding[1])
    label = tk.Label(frame, text=config["title"])
    label.pack(anchor="w")
    table = Table(frame, titles=config["columns"],
                  data=config["data"])
    table.pack(anchor="w")
    on_click = config["on_click"]
    if on_click:
        cache = (lambda *args, page=page,
                        cid=cid,
                        on_click=on_click:
                            on_click(page, cid))
        table.handle_row_selected(cache)
    parts = {"table": table, "label": label}
    return parts


def reader(page, cid):
    cache = page.components[cid]
    parts = cache["parts"]
    config = cache["config"]
    table = parts["table"]
    selection = table.selection
    if selection:
        selection = selection[0]["data"]
    return selection


def updater(page, cid, **config):  # TODO
    pass
