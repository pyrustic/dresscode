from dresscode.exception import DresscodeException
from pyrustic.app import App as PyrusticApp
from pyrustic.view import View
from pyrustic.widget.scrollbox import Scrollbox
from tk_cyberpunk_theme.main import Cyberpunk
import tkinter as tk


class App:
    def __init__(self, title=None, width=900, height=550,
                 home=None, scrollbar="vertical",
                 theme=Cyberpunk(), on_exit=None):
        self._title = title
        self._width = width
        self._height = height
        self._home = home
        self._scrollbar = scrollbar
        self._theme = theme
        self._on_exit = on_exit
        self._pages = {}
        self._opened_page = None
        self._menubar = None
        self._main_view = None
        self._menu_map = {}
        self._pids = []
        self._pids_count = 0
        self._pyrustic_app = PyrusticApp(None)
        self._root = self._pyrustic_app.root
        self._setup()

    @property
    def opened_page(self):
        return self._opened_page

    @property
    def pyrustic_app(self):
        return self._pyrustic_app

    @property
    def main_view(self):
        return self._main_view

    @property
    def root(self):
        return self._root

    def add_page(self, page, category=None):
        pid = page.pid
        if not pid:
            pid = self._gen_pid()
            page.pid = pid
        if pid in self._pages:
            message = "Duplicate page id isn't allowed ({})".format(pid)
            raise DresscodeException(message)
        self._pages[pid] = page
        self._pids.append(pid)
        self._main_view.populate_menubar(pid, page, category)
        page.app = self

    def open_page(self, pid):
        if pid not in self._pages:
            message = "You cannot open a page that you haven't added yet"
            raise DresscodeException(message)
        if self._opened_page:
            self._opened_page.destroy_page_view()
        page = self._pages[pid]
        self._opened_page = page
        scrollbox = self._main_view.body
        scrollbox.clear()
        page.install_page_view(scrollbox.box)

    def open_home(self):
        if self._home:
            self.open_page(self._home)

    def start(self):
        self._pyrustic_app.start()

    def _setup(self):
        # set theme
        if self._theme:
            self._pyrustic_app.theme = self._theme
        # set title
        if self._title:
            self._title = "{} | built with Pyrustic".format(self._title)
            self._pyrustic_app.root.title(self._title)
        # set width and height
        if self._width and self._height:
            cache = "{}x{}+0+0".format(self._width, self._height)
            self._pyrustic_app.root.geometry(cache)
        # center the app
        self._pyrustic_app.center()
        # set exit handler
        if self._on_exit:
            self._pyrustic_app.exit_handler = self._on_exit
        # set the main view
        self._main_view = _MainView(self, self._scrollbar)
        self._pyrustic_app.view = self._main_view

    def _gen_pid(self):
        self._pids_count += 1
        return "pid_{}".format(self._pids_count)


class _MainView(View):

    def __init__(self, app, scrollbar):
        super().__init__()
        self._app = app
        self._scrollbar = scrollbar
        self._root = app.root
        self._body = None
        self._menubar = None
        self._menu_cache = []
        self._menu_map = {}

    def _on_build(self):
        self._body = Scrollbox(self._root,
                               orient=self._scrollbar)
        # set menubar
        self._menubar = tk.Menu(self._root)
        self._root.config(menu=self._menubar)

    def _on_display(self):
        # consume menu cache
        for pid, page,category in self._menu_cache:
            self.populate_menubar(pid, page, category)
        if not self._app.opened_page:
            self._app.open_home()

    def populate_menubar(self, pid, page, category):
        if not self._body:
            data = (pid, page, category)
            self._menu_cache.append(data)
            return
        page_name = page.name
        menu = None
        command = (lambda self=self, pid=pid:
                   self._app.open_page(pid))
        if category:
            if category in self._menu_map:
                menu = self._menu_map[category]
            else:
                menu = tk.Menu(self._menubar, tearoff=0)
                self._menu_map[category] = menu
                self._menubar.add_cascade(label=category,
                                          menu=menu)
            menu.add_command(label=page_name,
                             command=command)
        else:
            if page_name in self._menu_map:
                menu = self._menu_map[page_name]
            else:
                menu = self._menubar
            menu.add_command(label=page_name,
                             command=command)
