import tkinter as tk


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
    show = None
    if config["secretive"]:
        show = "*"
    str_var = tk.StringVar()
    entry = tk.Entry(frame, show=show,
                     textvariable=str_var,
                     width=config["width"])
    entry.pack(anchor="w")
    on_submit = config["on_submit"]
    if config["text"]:
        str_var.set(config["text"])
    if on_submit:
        cache = (lambda e, page=page,
                        cid=cid,
                        on_submit=on_submit:
                            on_submit(page, cid))
        entry.bind("<Return>", cache)
    parts = {"entry": entry, "str_var": str_var,
             "label": label, "frame": frame}
    return parts, data_getter


def data_getter(page, cid):
    cache = page.components[cid]
    parts = cache["parts"]
    config = cache["config"]
    return parts["str_var"].get()
