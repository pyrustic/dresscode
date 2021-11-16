import tkinter as tk
from collections import namedtuple
from dresscode import Component


class Editor(Component):
    def __init__(self, page, cid):
        super().__init__(page, cid)
        self._box = None
        self._strvar_title = tk.StringVar()
        self._text_widget = None

    @property
    def parts(self):
        """Dictionary that contains parts of this component.
        Exposed parts are: "text_widget" and "strvar_title"
        """
        return self._parts

    def build(self, title=None, text=None, readonly=False,
              width=45, height=10,
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
        # create text widget
        from tkinter.scrolledtext import ScrolledText
        self._text_widget = ScrolledText(self._box, width=width, height=height)
        self._text_widget.pack(fill=fill, expand=expand)
        self._parts["text"] = self._text_widget
        # fill text widget
        if text is not None:
            self._text_widget.insert("1.0", text)
        if readonly:
            self._text_widget.config(state=tk.DISABLED)

    def read(self):
        if self._text_widget:
            return self._text_widget.get("1.0", tk.END)
        return None

    def update(self, title=None, text=None, readonly=None):
        if title is not None:
            self._strvar_title.set(title)
        if text is not None:
            readonly_cache = self._text_widget.cget("state")
            readonly_cache = True if readonly_cache == tk.DISABLED else False
            if readonly_cache:
                self._text_widget.config(state=tk.NORMAL)
            self._text_widget.delete("1.0", tk.END)
            self._text_widget.insert("1.0", text)
            if readonly_cache:
                self._text_widget.config(state=tk.DISABLED)
        if readonly is not None:
            state = tk.DISABLED if readonly else tk.NORMAL
            self._text_widget.config(state=state)

    def _gen_info(self):
        Info = namedtuple("Info", ("page", "cid", "component"))
        info = Info(self._page, self._cid, self)
        return info
