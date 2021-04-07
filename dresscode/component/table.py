import tkinter as tk
from pyrustic.widget.table import Table


def builder(page, cid):
    cache = page.components[cid]
    master = cache["master"]
    padding = cache["padding"]
    config = cache["config"]
    frame = tk.Frame(master)
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
    parts = {"table": table, "label": label, "frame": frame}
    return parts, data_getter


def data_getter(page, cid):
    print("GET DATA, ", cid)
    cache = page.components[cid]
    parts = cache["parts"]
    config = cache["config"]
    table = parts["table"]
    selection = table.selection
    if selection:
        selection = selection[0]["data"]
    return selection
