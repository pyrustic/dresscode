import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from viewable import Viewable
from megawidget import ScrollBox
from megawidget import Confirmation
from megawidget import Toast
from dresscode import error


class Page:
    def __init__(self, pid=None, name="Page",
                 scrolling="vertical",
                 on_open=None, on_close=None):
        self._pid = pid
        self._name = name
        self._scrolling = scrolling
        self._on_open = on_open
        self._on_close = on_close
        self._app = None
        self._view = None
        self._cids_count = 0
        self._components = {}
        self._cache = []
        self._todo_cache = []
        self._name = name if name else str(self._pid).capitalize()

    @property
    def pid(self):
        """Returns the page id"""
        return self._pid

    @pid.setter
    def pid(self, val):
        """Set the page id"""
        if self._pid and val != self._pid:
            raise error.AlreadyDefinedError
        self._pid = val

    @property
    def name(self):
        """Returns the page name"""
        return self._name

    @property
    def scrolling(self):
        """Returns the scrolling value"""
        return self._scrolling

    @property
    def on_open(self):
        return self._on_open

    @on_open.setter
    def on_open(self, val):
        self._on_open = val

    @property
    def on_close(self):
        return self._on_close

    @on_close.setter
    def on_close(self, val):
        self._on_close = val

    @property
    def app(self):
        """Returns the app reference"""
        return self._app

    @app.setter
    def app(self, val):
        """Set the app reference"""
        if self._app and val != self._app:
            raise error.AlreadyDefinedError
        self._app = val

    @property
    def view(self):
        """Returns the page view"""
        return self._view

    @property
    def components(self):
        """Returns the dictionary of components.
        The dictionary keys are CIDs (component id)"""
        return self._components.copy()

    def add(self, component_class, cid=None, **config):
        """
        Standard config: new_col, side, anchor, fill, padx and pady
        Component specific config: **specific_config
        """
        if not cid:
            cid = self.new_cid()
        if cid in self._components:
            raise error.DuplicateComponentError
        if not self._view:
            operation = {"name": "add",
                         "data":
                             {
                                 "component_class": component_class,
                                 "cid": cid,
                                 "config": config
                             }
                         }
            self._todo_cache.append(operation)
            return
        component = component_class(self, cid)
        self._components[cid] = component
        component.build(**config)
        return cid

    def read(self, cid):
        try:
            return self._components[cid].read()
        except KeyError as e:
            raise error.ComponentNotFoundError from None

    def update(self, cid, **config):
        try:
            return self._components[cid].update(**config)
        except KeyError as e:
            raise error.ComponentNotFoundError from None

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
            raise error.PageStateError("You must add this page to the app first")
        if orient == "x":
            self._app.main_view.body.xview_moveto(value)
        else:
            self._app.main_view.body.yview_moveto(value)

    def open(self):
        if not self._app:
            msg = "Add the page to the App instance first !"
            raise error.PageStateError(msg)
        if not self._view:
            self._view = View(self)
            self._view.build()
        self._view.body.pack(fill=tk.BOTH, expand=1, padx=0,
                             pady=(5, 0))
        if self._on_open:
            self._on_open(self)
        # consume todo
        self._consume_todo()

    def close(self):
        if self._app.caching:
            if self._on_close:
                self._on_close(self)
            self._view.body.pack_forget()
        else:
            self._view.body.pack_forget()
            self._view.destroy()
            self._view = None
            self._components = dict()

    def new_cid(self):
        self._cids_count += 1
        return "cid-{}".format(self._cids_count)

    def new_row(self, padx=0, pady=0, expand=False, fill=tk.X):
        if not self._view:
            operation = {"name": "new_row",
                         "data":
                             {
                                 "padx": padx,
                                 "pady": pady,
                                 "expand": expand,
                                 "fill": fill
                             }
                         }
            self._todo_cache.append(operation)
            return None
        return self._view.new_row(padx=padx, pady=pady,
                                  expand=expand, fill=fill)

    def new_box(self, new_col=True, side=tk.TOP, anchor=tk.CENTER,
                padx=5, pady=5, expand=False, fill=None):
        if not self._view:
            operation = {"name": "new_box",
                         "data":
                             {
                                 "new_col": new_col,
                                 "side": side,
                                 "anchor": anchor,
                                 "padx": padx,
                                 "pady": pady,
                                 "expand": expand,
                                 "fill": fill
                             }
                         }
            self._todo_cache.append(operation)
            return None
        return self._view.new_box(new_col=new_col, side=side,
                                  anchor=anchor, padx=padx, pady=pady,
                                  expand=expand, fill=fill)

    def _consume_todo(self):
        for operation in self._todo_cache:
            name, data = operation["name"], operation["data"]
            if name == "add":
                self.add(data["component_class"], data["cid"],
                         **data["config"])
            elif name == "new_row":
                self.new_row(padx=data["padx"], pady=data["pady"],
                             expand=data["expand"], fill=data["fill"])
            elif name == "new_box":
                self.new_box(new_col=data["new_col"], side=data["side"],
                             anchor=data["anchor"], padx=data["padx"],
                             pady=data["pady"], expand=data["expand"],
                             fill=data["fill"])
        if self._app.caching:
            self._todo_cache = []


class View(Viewable):
    def __init__(self, page):
        super().__init__()
        self._page = page
        self._master = page.app.view.body
        self._row = None
        self._col = None
        self._box = None
        self._rows = []
        self._cols = []
        self._boxes = []

    @property
    def page(self):
        return self._page

    @property
    def master(self):
        return self._master

    @property
    def row(self):
        return self._row

    @property
    def rows(self):
        return self._rows

    @property
    def col(self):
        return self._col

    @property
    def cols(self):
        return self._cols

    @property
    def box(self):
        return self._box

    @property
    def boxes(self):
        return self._boxes

    def new_row(self, padx=0, pady=0, expand=False, fill=tk.X):
        row = tk.Frame(self._body.box)
        row.pack(fill=fill, expand=expand, padx=padx, pady=pady)
        self._row = row
        self._rows.append(row)
        return row

    def new_col(self):
        col = tk.Frame(self._row)
        col.pack(side=tk.LEFT, fill=tk.Y, padx=0, pady=0)
        self._col = col
        self._cols.append(col)
        return col

    def new_box(self, new_col=True, side=tk.TOP, anchor=tk.CENTER,
                padx=5, pady=5, expand=False, fill=None):
        if not self._row:
            self.new_row()
        if not self._col or new_col:
            self.new_col()
        box = tk.Frame(self._col)
        box.pack(side=side, anchor=anchor, padx=padx, pady=pady,
                 expand=expand, fill=fill)
        if expand or fill:
            self._col.pack(expand=expand, fill=fill)
        self._box = box
        self._boxes.append(box)
        return box

    def _build(self):
        self._body = ScrollBox(self._master,
                               orient=self._page.scrolling)

    def _on_map(self):
        pass

    def _on_destroy(self):
        if self.page.on_close:
            self.page.on_close(self)
