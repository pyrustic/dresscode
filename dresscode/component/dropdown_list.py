import tkinter as tk


def builder(page, cid):
    info = page.components[cid]
    container = info["container"]
    config = info["config"]
    # title
    label = tk.Label(container, text=config["title"])
    label.pack(anchor="w")
    # command
    on_choice = config["on_choice"]
    command = None
    if on_choice:
        command = lambda e, page=page, cid=cid: on_choice(page, cid)
    # optionmenu
    str_var = tk.StringVar()
    items = config["items"]
    if items:
        option_menu = tk.OptionMenu(container, str_var,
                                    *items, command=command)
    else:
        option_menu = tk.OptionMenu(container, str_var,
                                    None, command=command)
    option_menu.pack(side=tk.LEFT)
    # default
    default = config["default"]
    if default is None:
        str_var.set(config["prompt"])
    else:
        str_var.set(items[default])
    parts = {"label": label,
             "option_menu": option_menu,
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
