import tkinter as tk


def builder(page, cid):
    cache = page.components[cid]
    master = cache["master"]
    padding = cache["padding"]
    config = cache["config"]
    button = tk.Button(master, text=config["text"])
    button.pack(side=config["side"], anchor=config["anchor"],
                padx=padding[0], pady=padding[1])
    on_click = config["on_click"]
    if on_click:
        cache = (lambda page=page,
                        cid=cid,
                        on_click=on_click:
                 on_click(page, cid))
        button.config(command=cache)
    parts = {"button": button}
    return parts, data_getter


def data_getter(page, cid):
    return None
