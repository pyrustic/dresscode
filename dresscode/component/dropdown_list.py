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
    # command
    on_choice = config["on_choice"]
    command = None
    if on_choice:
        command = lambda e, page=page, cid=cid: on_choice(page, cid)
    # optionmenu
    str_var = tk.StringVar()
    option_menu = tk.OptionMenu(frame, str_var, *config["items"],
                                command=command)
    option_menu.pack(side=tk.LEFT)
    # default
    default = config["default"]
    if default is None:
        str_var.set(config["prompt"])
    else:
        str_var.set(config["items"][default])
    parts = {"frame": frame, "label": label,
             "option_menu": option_menu,
             "str_var": str_var}
    return parts, data_getter


def data_getter(page, cid):
    cache = page.components[cid]
    parts = cache["parts"]
    config = cache["config"]
    text = parts["str_var"].get()
    index = None
    if text in config["items"]:
        index = config["items"].index(text)
    return index, text
