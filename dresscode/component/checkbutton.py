import tkinter as tk


def builder(page, cid):
    info = page.components[cid]
    container = info["container"]
    config = info["config"]
    # title
    label = tk.Label(container, text=config["title"])
    label.pack(anchor="w")
    # items container
    items_frame = tk.Frame(container)
    items_frame.pack(anchor="w")
    intvars = []
    checkbuttons = []
    # loop in items
    for item in config["items"]:
        int_var = tk.IntVar()
        intvars.append(int_var)
        checkbutton = tk.Checkbutton(items_frame,
                                     variable=int_var,
                                     onvalue=1, offvalue=0,
                                     text=item)
        checkbuttons.append(checkbutton)
        on_choice = config["on_choice"]
        if on_choice:
            command = (lambda page=page,
                              cid=cid,
                       on_choice=on_choice:
                        on_choice(page, cid))
            checkbutton.config(command=command)
        if config["stacking"] == "horizontal":
            checkbutton.pack(side=tk.LEFT, anchor="w")
        else:
            checkbutton.pack(anchor="w")
    # populate
    default = config["default"]
    if default is None:
        pass
    elif type(default) is int:
        intvars[default].set(1)
    else:
        for i in default:
            intvars[i].set(1)
    # parts
    parts = {"label": label, "items_frame": items_frame,
             "intvars": intvars, "checkbuttons": checkbuttons}
    return parts


def reader(page, cid):
    info = page.components[cid]
    parts = info["parts"]
    config = info["config"]
    intvars = parts["intvars"]
    selected_index = []
    for i, int_var in enumerate(intvars):
        if int_var.get() == 1:
            selected_index.append(i)
    selected_text = []
    items = config["items"]
    for index in selected_index:
        selected_text.append(items[index])
    return selected_index, selected_text


def updater(page, cid, **config): # TODO
    pass
