import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from viewable import Viewable
from megawidget.confirm import Confirm
from megawidget.toast import Toast
from dresscode.constant import COMPONENT_BUILDER, COMPONENT_READER, COMPONENT_UPDATER


class Page:
    def __init__(self, pid=None, name="Page", on_open=None,
                 on_close=None, padx=5, pady=5):
        self._pid = pid
        self._name = name
        self._on_open = on_open
        self._on_close = on_close
        self._padx = padx
        self._pady = pady
        self._app = None
        self._page_view = None
        self._cids_count = 0
        self._cache = []
        self._setup()

    @property
    def pid(self):
        """Returns the page id"""
        return self._pid

    @pid.setter
    def pid(self, val):
        """Set the page id (string)"""
        self._pid = val

    @property
    def name(self):
        """Returns the page name"""
        return self._name

    @property
    def app(self):
        """Returns the app reference"""
        return self._app

    @app.setter
    def app(self, val):
        """Set the app reference. You aren't supposed to use this property.
        When you add a page to the app instance, the app instance will use
        this property to set its reference."""
        self._app = val

    @property
    def root(self):
        """Returns the root Tk object if it's available, else returns None"""
        if not self._app:
            return None
        return self._app.pyrustic_app.root

    @property
    def page_view(self):
        """Returns the page view"""
        return self._page_view

    @property
    def components(self):
        """Returns the dictionary of components if it's available, else returns None.
        The dictionary keys are CIDs (component id)"""
        if not self._page_view:
            return None
        return self._page_view.components

    def show_text(self, message, title="Text", width=60, height=22):
        """Displays a text"""
        if not self._app:
            raise Error("You must add this page to the app first")
        text_view = _TextView(self.root, message, title, width, height)
        text_view.build()

    def show_toast(self, message, duration=1000):
        """Displays a toast that will last for x milliseconds (duration)"""
        if not self._app:
            raise Error("You must add this page to the app first")
        Toast(self.root, message=message, duration=duration)

    def ask_confirmation(self, title="Confirmation",
                         message="Attention required.\nDo you want to continue ?"):
        """Displays a confirmation dialog. Returns a boolean"""
        if not self._app:
            raise Error("You must add this page to the app first")
        confirm = Confirm(self.root, title=title, message=message)
        confirm.wait_window()
        return confirm.ok

    def scroll(self, orient="y", value=1):
        """
        Scrolls the page
        For orient = x:
            - 0: to scroll to left
            - 1: to scroll to right
        For orient = y:
            - 0: to scroll to top
            - 1: to scroll to bottom
        """
        if not self._app:
            raise Error("You must add this page to the app first")
        if orient == "x":
            self._app.main_view.body.xview_moveto(value)
        else:
            self._app.main_view.body.yview_moveto(value)

    def read_component(self, cid):
        """Returns the content of a component. Each component has
        a reader function that is invoked with the cid as argument.
        The returned value of the reader function is the one returned
        by the method read_component()"""
        if not self._page_view:
            raise Error("Please open the page first")
        if cid not in self._page_view.components:
            raise Error("Unknown component id")
        info = self._page_view.components[cid]
        reader = info["backend"]["reader"]
        return reader(self, cid)

    def update_component(self, cid, **config):
        if not self._page_view:
            raise Error("Please open the page first")
        if cid not in self._page_view.components:
            raise Error("Unknown component id")
        info = self._page_view.components[cid]
        updater = info["backend"]["updater"]
        cache = updater(self, cid, **config)
        for key, val in config.items():
            info["config"][key] = val
        return cache

    def remove_component(self, cid):
        if not self._page_view:
            raise Error("Please open the page first")
        if cid not in self._page_view.components:
            raise Error("Unknown component id")
        info = self._page_view.components[cid]
        container = info["container"]
        container.destroy()

    def add_custom(self, cid=None, new_row=False,
                   backend=None, **config):
        """ backend: a dict with keys: name, builder, reader, updater
        """
        config = {} if not config else config
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_space(self, cid=None, new_row=False, width=20, height=20,
                   side="left", anchor="center"):
        config = {"width": width, "height": height,
                  "side": side, "anchor": anchor}
        backend = {"name": "space", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_label(self, cid=None, new_row=False, text="Text",
                  color="tomato", font=("Courrier", 20),
                  side="left", anchor="n"):
        config = {"text": text, "color": color, "font": font,
                  "side": side, "anchor": anchor}
        backend = {"name": "label", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_entry(self, cid=None, new_row=False, title=None,
                  text=None, width=20, secretive=False,
                  on_submit=None, side="left", anchor="s"):
        config = {"title": title,
                  "text": text,
                  "width": width,
                  "secretive": secretive,
                  "on_submit": on_submit,
                  "side": side,
                  "anchor": anchor}
        backend = {"name": "entry", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_button(self, cid=None, new_row=False, text="Submit",
                   on_click=None, side="left", anchor="s", style=None):
        config = {"text": text,
                  "on_click": on_click,
                  "side": side,
                  "anchor": anchor,
                  "style": style}
        backend = {"name": "button", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_editor(self, cid=None, new_row=False, title=None,
                   text=None, readonly=False, width=45, height=10,
                   fill_row=False, side="left", anchor="s"):
        config = {"title": title,
                  "text": text,
                  "readonly": readonly,
                  "width": width,
                  "height": height,
                  "fill_row": fill_row,
                  "side": side,
                  "anchor": anchor}
        backend = {"name": "editor", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_checkbutton(self, cid=None, new_row=False, title=None,
                        items=None, default=None, stacking="horizontal",
                        on_choice=None, side="left", anchor="s"):
        config = {"title": title,
                  "items": [] if not items else items,
                  "default": default,
                  "stacking": stacking,
                  "on_choice": on_choice,
                  "side": side,
                  "anchor": anchor}
        backend = {"name": "checkbutton", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_radiobutton(self, cid=None, title=None, items=None,
                        default=None, stacking="horizontal",
                        new_row=False, side="left", anchor="s",
                        on_choice=None):
        config = {"title": title,
                  "items": [] if not items else items,
                  "default": default,
                  "stacking": stacking,
                  "on_choice": on_choice,
                  "side": side,
                  "anchor": anchor}
        backend = {"name": "radiobutton", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_spinbox(self, cid=None, new_row=False, title=None,
                    items=None, default=None, prompt="- Select -",
                    on_submit=None, side="left", anchor="s"):
        config = {"title": title,
                  "items": [] if not items else items,
                  "default": default,
                  "prompt": prompt,
                  "on_submit": on_submit,
                  "side": side,
                  "anchor": anchor}
        backend = {"name": "spinbox", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_dropdown_list(self, cid=None, new_row=False,
                          title=None, items=None, default=None,
                          prompt="- Select -", on_choice=None,
                          side="left", anchor="s"):
        config = {"title": title,
                  "items": [] if not items else items,
                  "default": default,
                  "prompt": prompt,
                  "on_choice": on_choice,
                  "side": side,
                  "anchor": anchor}
        backend = {"name": "dropdown_list", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_path_entry(self, cid=None, new_row=False,
                       title=None, text=None, browse="file",
                       width=17, on_submit=None,
                       side="left", anchor="s"):
        config = {"title": title,
                  "text": text,
                  "browse": browse,
                  "width": width,
                  "on_submit": on_submit,
                  "side": side,
                  "anchor": anchor}
        backend = {"name": "path_entry", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_image(self, cid=None, new_row=False,
                  title=None, image=None, width=0, height=0,
                  on_click=None, side="left", anchor="s"):
        config = {"title": title,
                  "image": image,
                  "width": width,
                  "height": height,
                  "on_click": on_click,
                  "side": side,
                  "anchor": anchor}
        backend = {"name": "image", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def add_table(self, cid=None, new_row=False, title=None,
                  columns=None, data=None, on_click=None,
                  side="left", anchor="s"):
        config = {"title": title,
                  "columns": columns,
                  "data": data,
                  "on_click": on_click,
                  "side": side,
                  "anchor": anchor}
        backend = {"name": "table", "builder": None,
                   "reader": None, "updater": None}
        self._add_component(cid=cid, new_row=new_row,
                            backend=backend, config=config)

    def install_page_view(self, master):
        #if self._page_view:
        #    self._page_view.destroy()
        new_page_view = False
        if not self._page_view:
            new_page_view = True
            self._page_view = _PageView(master, self,
                                        self._padx,
                                        self._pady)
            self._page_view.build()
        self._page_view.body.pack(fill=tk.BOTH, expand=1)
        if new_page_view:
            self._consume_cache()
        if self._on_open:
            self._on_open(self)

    def destroy_page_view(self):
        if self._page_view:
            self._page_view.destroy()
            self._page_view = None
            if self._on_close:
                self._on_close(self)

    def remove_page_view(self):
        if self._page_view:
            self._page_view.body.pack_forget()
            if self._on_close:
                self._on_close(self)

    # ===================================
    #              PRIVATE
    # ===================================

    def _setup(self):
        if not self._name:
            self._name = str(self._pid).capitalize()

    def _add_component(self, cid=None, new_row=None,
                       backend=None, config=None):
        if not backend:
            text = "Missing backend for the component '{}' !".format(cid)
            raise MissingBackendError(text)
        if not cid:
            cid = self._gen_cid()
        data = (cid, new_row, backend, config)
        if self._page_view:
            self._page_view.add_component(cid, new_row,
                                          backend, config)
        else:
            self._cache.append(data)

    def _consume_cache(self):
        for cid, new_row, backend, config in self._cache:
            self._page_view.add_component(cid, new_row,
                                          backend, config)

    def _gen_cid(self):
        self._cids_count += 1
        return "cid_{}".format(self._cids_count)


class _PageView(Viewable):

    def __init__(self, master, page,
                 padx, pady):
        super().__init__()
        self._master = master
        self._page = page
        self._padx = padx
        self._pady = pady
        self._row = None
        self._components = {}

    @property
    def components(self):
        return self._components

    def add_component(self, cid, new_row, backend, config):
        if cid and cid in self._components:
            raise Error("This component id already exists !")
        row = self._get_row()
        if new_row:
            row = self._get_new_row()
        padding = (self._padx, 0)
        container = self._create_container(row, padding, config)
        info = {"new_row": new_row, "backend": None,
                "config": config,   "container": container,
                "padding": padding, "parts": None}
        self._components[cid] = info
        backend = self._check_backend(backend)
        self._components[cid]["backend"] = backend
        builder = backend["builder"]
        # build component
        parts = builder(self._page, cid)
        self._components[cid]["parts"] = parts

    def _build(self):
        self._body = tk.Frame(self._master)

    def _get_row(self):
        if not self._row:
            self._row = tk.Frame(self._body)
            self._row.pack(fill=tk.X, padx=0,
                           pady=self._pady)
        return self._row

    def _get_new_row(self):
        self._row = None
        return self._get_row()

    def _check_backend(self, backend):
        name = backend["name"]
        builder = backend["builder"]
        reader = backend["reader"]
        updater = backend["updater"]
        # check builder
        if not builder:
            builder = COMPONENT_BUILDER.get(name, None)
        if not builder:
            message = "Missing builder for the component '{}' !".format(name)
            raise MissingBuilderError(message)
        # check reader
        if not reader:
            reader = COMPONENT_READER.get(name, None)
        if not reader:
            message = "Missing reader for the component '{}' !".format(name)
            raise MissingReaderError(message)
        # check updater
        if not updater:
            updater = COMPONENT_UPDATER.get(name, None)
        if not updater:
            message = "Missing updater for the component '{}' !".format(name)
            raise MissingUpdaterError(message)
        # all right
        return {"name": name,       "builder": builder,
                "reader": reader,   "updater": updater}

    def _create_container(self, master, padding, config):
        side = config.get("side", "left")
        anchor = config.get("anchor", "s")
        frame = tk.Frame(master)
        frame.pack(side=side, anchor=anchor,
                   padx=padding[0], pady=padding[1])
        return frame


class _TextView(Viewable):
    def __init__(self, master, message, title, width, height):
        super().__init__()
        self._master = master
        self._message = message
        self._title = title
        self._width = width
        self._height = height
        self._body = None
        self._scrolled_text = None

    def _build(self):
        self._body = tk.Toplevel(self._master)
        self._body.title(self._title)
        self._scrolled_text = ScrolledText(self._body, width=self._width,
                                           height=self._height)
        self._scrolled_text.pack()

    def _on_map(self):
        super()._on_map()
        self._scrolled_text.insert("1.0", self._message)
        self._scrolled_text.config(state="disabled")


class Error(Exception):
    def __init__(self, *args, **kwargs):
        self.code = 0
        self.message = args[0] if args else ""
        super().__init__(self.message)

    def __str__(self):
        return self.message


class MissingBackendError(Error):
    pass


class MissingBuilderError(Error):
    pass


class MissingReaderError(Error):
    pass


class MissingUpdaterError(Error):
    pass
