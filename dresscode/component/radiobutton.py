import tkinter as tk


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
    items_frame = tk.Frame(frame)
    items_frame.pack(anchor="w")
    int_vars = []
    radiobuttons = []
    int_var = tk.IntVar()
    # loop in items
    for i, item in enumerate(config["items"]):
        radiobutton = tk.Radiobutton(items_frame,
                                     variable=int_var,
                                     value=i,
                                     text=item)
        radiobuttons.append(radiobutton)
        on_choice = config["on_choice"]
        if on_choice:
            command = (lambda page=page,
                              cid=cid,
                       on_choice=on_choice:
                        on_choice(page, cid))
            radiobutton.config(command=command)
        if config["stacking"] == "horizontal":
            radiobutton.pack(side=tk.LEFT, anchor="w")
        else:
            radiobutton.pack(anchor="w")
    # populate
    default = config["default"]
    if default is None:
        pass
    else:
        int_var.set(default)
    # parts
    parts = {"label": label, "frame": frame, "items_frame": items_frame,
             "int_var": int_var, "radiobuttons": radiobuttons}
    return parts


def reader(page, cid):
    cache = page.components[cid]
    parts = cache["parts"]
    config = cache["config"]
    index = parts["int_var"].get()
    text = None
    if index is not None:
        text = config["items"][index]
    return index, text


def updater(page, cid, **config):  # TODO
    pass
