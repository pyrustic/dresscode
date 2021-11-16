import tkinter as tk
from dresscode import Component


class Entry(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._box = None
        self._strvar = tk.StringVar()

    def build(self, title="Entry field", width=20,
              secretive=False, on_submit=None,
              new_col=True, side=tk.LEFT, anchor="nw",
              padx=5, pady=5, expand=False, fill=None):
        self._box = self._page.new_box(new_col, side, anchor, padx, pady,
                                       expand, fill)
        label = tk.Label(self._box, text=title)
        label.pack(anchor="w", fill=fill, pady=(0, 2))
        entry = tk.Entry(self._box, width=width, textvariable=self._strvar)
        entry.pack(anchor="w", fill=fill)
        self._parts["label"] = label
        self._parts["entry"] = entry
        self._parts["strvar"] = self._strvar

    def read(self):
        pass

    def update(self, **config):
        pass
