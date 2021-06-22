import tkinter as tk


def builder(page, cid):
    info = page.components[cid]
    container = info["container"]
    config = info["config"]
    text_strvar = tk.StringVar()
    text = config["text"]
    if text:
        text_strvar.set(text)
    button = tk.Button(container, textvariable=text_strvar)
    button.pack(anchor="w")
    style = config["style"]
    if style:
        style.target(button)
    on_click = config["on_click"]
    if on_click:
        cache = (lambda page=page,
                        cid=cid,
                        on_click=on_click:
                 on_click(page, cid))
        button.config(command=cache)
    parts = {"button": button, "text_strvar": text_strvar}
    return parts


def reader(page, cid):
    return None


def updater(page, cid, **config):
    info = page.components[cid]
    if "text" in config:
        text = config["text"]
        # update info
        info["config"]["text"] = text  # TODO useless, remove this line (update_component already do it)
        # update widget
        text_strvar = info["parts"]["text_strvar"]
        text_strvar.set(text)
    if "on_click" in config:
        on_click = config["on_click"]
        # update info
        info["config"]["on_click"] = on_click # TODO useless, remove this line (update_component already do it)
        # update widget
        info["parts"]["button"].config(command=on_click)
