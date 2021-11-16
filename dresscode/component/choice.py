import tkinter as tk
from collections import namedtuple
from dresscode import Component
import megawidget


class Choice(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._box = None
        self._choice = None
        self._strvar_title = tk.StringVar()

    @property
    def parts(self):
        """Dictionary that contains parts of this component.
        Exposed parts are: "choice" and "strvar_title"
        """
        return self._parts

    def build(self, title=None, items=None, selection=None, flavor="radio",
              stacking="vertical", on_change=None,
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
        # set on_change
        if on_change:
            info = self._gen_info()
            command = (lambda choice, on_change=on_change, info=info: on_change(info))
        else:
            command = None
        # create choice megawidget
        self._choice = megawidget.Choice(self._box, items=items, selection=selection,
                                         flavor=flavor, stacking=stacking,
                                         on_change=command)
        self._choice.pack(fill=fill, expand=expand)
        self._parts["choice"] = self._choice

    def read(self):
        if self._choice:
            return self._choice.selection
        return None

    def update(self, title=None):
        if title is not None:
            self._strvar_title.set(title)

    def _gen_info(self):
        Info = namedtuple("Info", ("page", "cid", "component"))
        info = Info(self._page, self._cid, self)
        return info
