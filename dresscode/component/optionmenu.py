import tkinter as tk
from collections import namedtuple
from dresscode import Component


class OptionMenu(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._box = None
        self._button = None
        self._icon = None
        self._strvar_title = tk.StringVar()
        self._strvar_selection = tk.StringVar()

    @property
    def parts(self):
        """Dictionary that contains parts of this component.
        Exposed parts are: "items", "strvar_title" and "option_menu"
        """
        return self._parts

    def build(self, title=None, items=None, prompt="- Select -",
              selection=None, on_select=None,
              new_col=True, side=tk.BOTTOM, anchor="nw",
              padx=5, pady=5, expand=False, fill=None):
        # get new box
        self._box = self._page.new_box(new_col, side, anchor, padx, pady,
                                       expand, fill)
        # set title
        if title:
            self._strvar_title.set(title)
            title_label = tk.Label(self._box, textvariable=self._strvar_title)
            title_label.pack(anchor="nw")
        self._parts["strvar_title"] = self._strvar_title
        # set default selection
        if selection is None:
            self._strvar_selection.set(prompt)
        else:
            self._strvar_selection.set(items[selection])
        # on_select handler
        if on_select:
            info = self._gen_info()
            command = lambda event, on_select=on_select, info=info: on_select(info)
        else:
            command = None
        # create OptionMenu widget
        if items:
            self._option_menu = tk.OptionMenu(self._box, self._strvar_selection,
                                              *items, command=command)
        else:
            self._option_menu = tk.OptionMenu(self._box, self._strvar_selection,
                                              "", command=command)
        self._items = items
        self._option_menu.pack(fill=fill, expand=expand)
        self._option_menu.config(relief="flat", borderwidth=0, highlightthickness=0)
        self._parts["option_menu"] = self._option_menu

    def read(self):
        str_selection = self._strvar_selection.get()
        index = None
        if not self._items:
            return None
        if str_selection in self._items:
            index = self._items.index(str_selection)
        return index

    def update(self, title=None):
        # update title
        if title is not None:
            self._strvar_title.set(title)

    def _gen_info(self):
        Info = namedtuple("Info", ("page", "cid", "component"))
        info = Info(self._page, self._cid, self)
        return info
