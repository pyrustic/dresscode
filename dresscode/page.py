import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from pyrustic.view import View
from pyrustic.widget.confirm import Confirm
from pyrustic.widget.toast import Toast
from dresscode.exception import DresscodeException
from dresscode.constant import COMPONENT_BUILDER


class Page:
    def __init__(self, pid=None, name=None, on_display=None,
                 on_destroy=None, padx=5, pady=5):
        self._pid = pid
        self._name = name
        self._on_display = on_display
        self._on_destroy = on_destroy
        self._padx = padx
        self._pady = pady
        self._app = None
        self._page_view = None
        self._cids_count = 0
        self._cache = []
        self._setup()

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, val):
        self._pid = val

    @property
    def name(self):
        return self._name

    @property
    def app(self):
        return self._app

    @app.setter
    def app(self, val):
        self._app = val

    @property
    def root(self):
        if not self._app:
            return None
        return self._app.pyrustic_app.root

    @property
    def page_view(self):
        return self._page_view

    @property
    def components(self):
        if not self._page_view:
            return None
        return self._page_view.components

    def show_text(self, message, title="Text", width=60, height=22):
        if not self._app:
            raise DresscodeException("You must add this page to the app first")
        text_view = _TextView(self.root, message, title, width, height)
        text_view.build()

    def show_toast(self, message, duration=1000):
        if not self._app:
            raise DresscodeException("You must add this page to the app first")
        Toast(self.root, message=message, duration=duration)

    def ask_confirmation(self, title="Confirmation",
                         message="Attention required.\nDo you want to continue ?"):
        if not self._app:
            raise DresscodeException("You must add this page to the app first")
        confirm = Confirm(self.root, title=title, message=message)
        confirm.wait_window()
        return confirm.ok

    def get_data(self, cid):
        if not self._page_view:
            raise DresscodeException("Please add the page to the app first")
        if cid not in self._page_view.components:
            raise DresscodeException("Unknown component id")
        cache = self._page_view.components[cid]
        data_getter = cache["data_getter"]
        data = data_getter(self, cid)
        return data

    def scroll(self, orient="y", value=1):
        """ For x:
            - 0: to scroll to left
            - 1: to scroll to right
            For y:
            - 0: to scroll to top
            - 1: to scroll to bottom
        """
        if not self._app:
            raise DresscodeException("You must add this page to the app first")
        if orient == "x":
            self._app.main_view.body.xview_moveto(value)
        else:
            self._app.main_view.body.yview_moveto(value)

    def add_custom(self, cid=None, name=None,
                   builder=None, config=None,
                   new_row=False):
        config = {} if not config else config
        self._add_component(cid=cid, name=name,
                            builder=builder,
                            config=config,
                            new_row=new_row)

    def add_space(self, cid=None, width=20, height=20,
                  new_row=False, side="left", anchor="center"):
        config = {"width": width, "height": height,
                  "side": side,
                  "anchor": anchor}
        self._add_component(cid=cid, name="space", config=config,
                            new_row=new_row)

    def add_label(self, cid=None, color="tomato", text="Text", font=("Courrier", 20),
                  new_row=False, side="left", anchor="center"):
        config = {"text": text, "font": font, "color": color,
                  "side": side,
                  "anchor": anchor, "new_row": new_row}
        self._add_component(cid=cid, name="label", config=config,
                            new_row=new_row)

    def add_entry(self, cid=None, title=None,
                  text=None, width=20,
                  new_row=False, side="left", anchor="sw",
                  secretive=False, on_submit=None):
        config = {"title": title,
                  "width": width,
                  "text": text,
                  "new_row": new_row,
                  "secretive": secretive,
                  "on_submit": on_submit,
                  "side": side,
                  "anchor": anchor}
        self._add_component(cid=cid, name="entry", config=config,
                            new_row=new_row)

    def add_button(self, cid=None, text="Submit",
                   new_row=False, side="left", anchor="s",
                   on_click=None):
        config = {"text": text,
                  "new_row": new_row,
                  "on_click": on_click,
                  "side": side,
                  "anchor": anchor}
        self._add_component(cid=cid, name="button", config=config,
                            new_row=new_row)

    def add_editor(self, cid=None, title=None, text=None,
                   width=45, height=10, fill_row=False,
                   readonly=False,
                   new_row=False, side="left", anchor="s"):
        config = {"title": title,
                  "text": text,
                  "width": width,
                  "height": height,
                  "fill_row": fill_row,
                  "readonly": readonly,
                  "new_row": new_row,
                  "side": side,
                  "anchor": anchor}
        self._add_component(cid=cid, name="editor", config=config,
                            new_row=new_row)

    def add_checkbutton(self, cid=None, title=None, items=None,
                        default=None, stacking="horizontal",
                        new_row=False, side="left", anchor="s",
                        on_choice=None):
        config = {"title": title,
                  "items": [] if not items else items,
                  "default": default,
                  "stacking": stacking,
                  "new_row": new_row,
                  "side": side,
                  "anchor": anchor,
                  "on_choice": on_choice}
        self._add_component(cid=cid, name="checkbutton", config=config,
                            new_row=new_row)

    def add_radiobutton(self, cid=None, title=None, items=None,
                        default=None, stacking="horizontal",
                        new_row=False, side="left", anchor="s",
                        on_choice=None):
        config = {"title": title,
                  "items": [] if not items else items,
                  "default": default,
                  "stacking": stacking,
                  "new_row": new_row,
                  "side": side,
                  "anchor": anchor,
                  "on_choice": on_choice}
        self._add_component(cid=cid, name="radiobutton", config=config,
                            new_row=new_row)

    def add_spinbox(self, cid=None, title=None, items=None,
                    prompt="- Select -", default=None, new_row=False, side="left",
                    anchor="s", on_submit=None):
        config = {"title": title,
                  "items": [] if not items else items,
                  "default": default,
                  "prompt": prompt,
                  "new_row": new_row,
                  "side": side,
                  "anchor": anchor,
                  "on_submit": on_submit}
        self._add_component(cid=cid, name="spinbox", config=config,
                            new_row=new_row)

    def add_dropdown_list(self, cid=None, title=None, items=None,
                          default=None, prompt="- Select -",
                          new_row=False, side="left",
                          anchor="s", on_choice=None):
        config = {"title": title,
                  "items": [] if not items else items,
                  "default": default,
                  "prompt": prompt,
                  "new_row": new_row,
                  "side": side,
                  "anchor": anchor,
                  "on_choice": on_choice}
        self._add_component(cid=cid, name="dropdown_list", config=config,
                            new_row=new_row)

    def add_path_entry(self, cid=None, title=None,
                       text=None, width=17,
                       new_row=False, side="left", anchor="s",
                       browse="file", on_submit=None):
        config = {"title": title,
                  "text": text,
                  "width": width,
                  "new_row": new_row,
                  "browse": browse,
                  "side": side,
                  "anchor": anchor,
                  "on_submit": on_submit}
        self._add_component(cid=cid, name="path_entry", config=config,
                            new_row=new_row)

    def add_image(self, cid=None, title=None,
                  image=None, width=0, height=0,
                  new_row=False, side="left", anchor="sw",
                  on_click=None):
        config = {"title": title,
                  "image": image,
                  "width": width,
                  "height": height,
                  "new_row": new_row,
                  "side": side,
                  "anchor": anchor,
                  "on_click": on_click}
        self._add_component(cid=cid, name="image", config=config,
                            new_row=new_row)

    def add_table(self, cid=None, title=None,
                  data=None, new_row=False, columns=None,
                  side="left", anchor="sw", on_click=None):
        config = {"title": title,
                  "columns": columns,
                  "data": data,
                  "new_row": new_row,
                  "side": side,
                  "anchor": anchor,
                  "on_click": on_click}
        self._add_component(cid=cid, name="table", config=config,
                            new_row=new_row)

    def install_page_view(self, master):
        if self._page_view:
            self._page_view.destroy()
        self._page_view = _PageView(master, self,
                                    self._padx,
                                    self._pady,
                                    self._on_display,
                                    self._on_destroy)
        self._page_view.build_pack(fill=tk.BOTH, expand=1)
        self._consume_cache()

    def destroy_page_view(self):
        if self._page_view:
            self._page_view.destroy()
            self._page_view = None

    # ===================================
    #              PRIVATE
    # ===================================

    def _setup(self):
        if not self._name:
            self._name = str(self._pid).capitalize()

    def _add_component(self, cid=None, name=None,
                       builder=None, config=None,
                       new_row=None):
        if not cid:
            cid = self._gen_cid()
        data = (cid, name, builder, config,
                new_row)
        if self._page_view:
            self._page_view.add_component(cid, name, builder,
                                          config, new_row)
        else:
            self._cache.append(data)

    def _consume_cache(self):
        for cid, name, builder, config, new_row in self._cache:
            self._page_view.add_component(cid, name,
                                          builder, config,
                                          new_row)

    def _gen_cid(self):
        self._cids_count += 1
        return "cid_{}".format(self._cids_count)


class _PageView(View):

    def __init__(self, master, page,
                 padx, pady, on_display,
                 on_destroy):
        super().__init__()
        self._master = master
        self._page = page
        self._padx = padx
        self._pady = pady
        self._on_display_handler = on_display
        self._on_destroy_handler = on_destroy
        self._row = None
        self._components = {}
        self._name_widget_map = None
        self._cache = []

    @property
    def components(self):
        return self._components

    def add_component(self, cid, name, builder,
                      config, new_row):
        if cid and cid in self._components:
            raise DresscodeException("This component id already exists !")
        row = self._get_row()
        if new_row:
            row = self._get_new_row()
        padding = (self._padx, 0)
        self._components[cid] = {"name": name,
                                 "master": row,
                                 "padding": padding,
                                 "builder": builder,
                                 "config": config,
                                 "parts": None,
                                 "data_getter": None}
        parts, data_getter = self._build_component(cid, name, builder)
        self._components[cid]["parts"] = parts
        self._components[cid]["data_getter"] = data_getter

    def _on_build(self):
        self._body = tk.Frame(self._master)

    def _on_display(self):
        if self._on_display_handler:
            self._on_display_handler(self._page)

    def _on_destroy(self):
        if self._on_destroy_handler:
            self._on_destroy_handler(self._page)

    def _build_component(self, cid, name, builder):
        if not builder:
            builder = COMPONENT_BUILDER.get(name, None)
        if not builder:
            message = "Missing builder for the component '{}'!".format(name)
            raise DresscodeException(message)
        cache = builder(self._page, cid)
        parts, data_getter = None, None
        try:
            parts, data_getter = cache
        except Exception as e:
            text = "The builder {} should return a 2-tuple".format(name)
            raise DresscodeException(text)
        return parts, data_getter

    def _get_row(self):
        if not self._row:
            self._row = tk.Frame(self._body)
            self._row.pack(fill=tk.X, padx=0,
                           pady=self._pady)
        return self._row

    def _get_new_row(self):
        self._row = None
        return self._get_row()


class _TextView(View):
    def __init__(self, master, message, title, width, height):
        super().__init__()
        self._master = master
        self._message = message
        self._title = title
        self._width = width
        self._height = height
        self._body = None
        self._scrolled_text = None

    def _on_build(self):
        self._body = tk.Toplevel(self._master)
        self._body.title(self._title)
        self._scrolled_text = ScrolledText(self._body, width=self._width,
                                           height=self._height)
        self._scrolled_text.pack()

    def _on_display(self):
        self._scrolled_text.insert("1.0", self._message)
        self._scrolled_text.config(state="disabled")
