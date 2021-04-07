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
    checkbuttons = []
    # loop in items
    for item in config["items"]:
        int_var = tk.IntVar()
        int_vars.append(int_var)
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
        int_vars[default].set(1)
    else:
        for i in default:
            int_vars[i].set(1)
    # parts
    parts = {"label": label, "frame": frame, "items_frame": items_frame,
             "int_vars": int_vars, "checkbuttons": checkbuttons}
    return parts, data_getter


def data_getter(page, cid):
    cache = page.components[cid]
    parts = cache["parts"]
    config = cache["config"]
    int_vars = parts["int_vars"]
    selected_index = []
    for i, int_var in enumerate(int_vars):
        if int_var.get() == 1:
            selected_index.append(i)
    selected_text = []
    items = config["items"]
    for index in selected_index:
        selected_text.append(items[index])
    return selected_index, selected_text
