import tkinter as tk


def builder(page, cid):
    cache = page.components[cid]
    master = cache["master"]
    padding = cache["padding"]
    config = cache["config"]
    frame = tk.Frame(master)
    fill = None
    expand = 0
    if config["fill_row"]:
        fill = tk.X
        expand = 1
    frame.pack(side=config["side"], anchor=config["anchor"],
               padx=padding[0], pady=padding[1],
               fill=fill, expand=expand)
    label = tk.Label(frame, text=config["title"])
    label.pack(anchor="w")
    text = tk.Text(frame, width=config["width"],
                   height=config["height"])
    text.pack(anchor="w", fill=fill, expand=expand)
    text_input = config["text"]
    if text_input:
        text.insert("1.0", text_input)
    if config["readonly"]:
        text.config(state="disabled")
    parts = {"frame": frame, "label": label,
             "text": text}
    return parts, data_getter


def data_getter(page, cid):
    cache = page.components[cid]
    parts = cache["parts"]
    config = cache["config"]
    return parts["text"].get("1.0", 'end-1c')
