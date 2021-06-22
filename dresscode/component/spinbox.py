import tkinter as tk


def builder(page, cid):
    info = page.components[cid]
    container = info["container"]
    padding = info["padding"]
    config = info["config"]
    # container
    frame = tk.Frame(container)
    frame.pack(side=config["side"], anchor=config["anchor"],
               padx=padding[0], pady=padding[1])
    # title
    label = tk.Label(frame, text=config["title"])
    label.pack(anchor="w")
    # spinbox
    str_var = tk.StringVar()
    spinbox = tk.Spinbox(frame, textvariable=str_var,
                         values=config["items"])
    spinbox.pack(side=tk.LEFT)
    # default
    default = config["default"]
    if default is None:
        str_var.set(config["prompt"])
    else:
        str_var.set(config["items"][default])
    # command
    on_submit = config["on_submit"]
    if on_submit:
        command = lambda e, page=page, cid=cid: on_submit(page, cid)
        spinbox.bind("<Return>", command)
    parts = {"frame": frame, "label": label, "spinbox": spinbox,
             "str_var": str_var}
    return parts


def reader(page, cid):
    info = page.components[cid]
    parts = info["parts"]
    config = info["config"]
    text = parts["str_var"].get()
    index = None
    if text in config["items"]:
        index = config["items"].index(text)
    return index, text


def updater(page, cid, **config):  # TODO
    pass
