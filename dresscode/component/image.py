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
    image = config["image"]
    width = 0 if config["width"] is None else config["width"]
    height = 0 if config["height"] is None else  config["height"]
    photo_image = tk.PhotoImage(data=image,
                                width=width,
                                height=height)
    canvas = tk.Canvas(frame,
                       width=photo_image.width(),
                       height=photo_image.height())
    canvas.pack(anchor="w")
    canvas.create_image(0, 0, image=photo_image, anchor="nw")
    on_click = config["on_click"]
    if on_click:
        cache = (lambda e, page=page,
                        cid=cid,
                        on_click=on_click:
                            on_click(page, cid))
        canvas.bind("<Button-1>", cache)
    parts = {"label": label, "canvas": canvas,
             "photo_image": photo_image, "frame": frame}
    return parts


def reader(page, cid):
    return None


def updater(page, cid, **config):  # TODO
    pass
