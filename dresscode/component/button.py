import tkinter as tk
from collections import namedtuple
from dresscode import Component


class Button(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._box = None
        self._button = None
        self._icon = None
        self._strvar = tk.StringVar()

    @property
    def parts(self):
        """Dictionary that contains parts of this component.
        Exposed parts are: "icon", "button" and "strvar_text"
        """
        return self._parts

    def build(self, text="Submit", icon=None, compound=tk.LEFT,
              on_click=None, style=None, state="normal",
              new_col=True, side=tk.BOTTOM, anchor="nw",
              padx=5, pady=5, expand=False, fill=None):
        # get new box
        self._box = self._page.new_box(new_col, side, anchor, padx, pady,
                                       expand, fill)
        # keep a reference to icon
        self._icon = icon
        self._parts["icon"] = icon
        # fill text stringvar
        if text:
            self._strvar.set(text)
        self._parts["strvar_text"] = self._strvar
        # on_click handler
        if on_click:
            info = self._gen_info()
            command = lambda on_click=on_click, info=info: on_click(info)
        else:
            command = None
        # create button
        self._button = tk.Button(self._box, textvariable=self._strvar,
                                 command=command, image=icon, compound=compound,
                                 state=state)
        self._button.pack(fill=fill, expand=expand)
        self._parts["button"] = self._button
        # styling
        if style:
            style.target(self._button)

    def read(self):
        return None

    def update(self, text=None, style=None,
               state=None):
        # update text
        if text is not None:
            self._strvar.set(text)
        # update style
        if style is not None:
            style.target(self._button)
        # update state
        if state is not None:
            self._button.config(state=state)

    def _gen_info(self):
        Info = namedtuple("Info", ("page", "cid", "component"))
        info = Info(self._page, self._cid, self)
        return info
