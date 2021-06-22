import tkinter as tk
from viewable import Viewable
from pyrustic.app import App as PyrusticApp
from cyberpunk_theme import Cyberpunk
from megawidget.scrollbox import Scrollbox


class App:
    """This is the entry point of your Dresscode app"""
    def __init__(self, title=None, width=900, height=550,
                 home=None, scrollbar="vertical",
                 theme=Cyberpunk(), on_exit=None):
        """
        Parameters
        ==========
        - title: string, the title of the app
        - width: int, the width of the app
        - height: int, the height of the app
        - home: string, the page id of the home page
        - scrollbar: the orient of the scrollbar, "vertical", "horizontal", "both".
        - theme: the theme, ie an instance of themebase.Theme
        - on_exit: the on_exit handler, ie a function that will be called on exit.
        """
        self._title = title
        self._width = width
        self._height = height
        self._home = home
        self._scrollbar = scrollbar
        self._theme = theme
        self._on_exit = on_exit
        self._pages = {}
        self._opened_page = None
        self._caching = False
        self._cache = {}
        self._menubar = None
        self._main_view = None
        self._menu_map = {}
        self._pids = []
        self._pids_count = 0
        self._pyrustic_app = PyrusticApp()
        self._root = self._pyrustic_app.root
        self._setup()

    @property
    def title(self):
        """Return the title of the app"""
        return self._title

    @title.setter
    def title(self, val):
        """Set the title of the app"""
        self._title = val

    @property
    def width(self):
        """Return the width of the app"""
        return self._width

    @width.setter
    def width(self, val):
        """Set the width of the app"""
        self._width = val

    @property
    def height(self):
        """Return the height of the app"""
        return self._height

    @height.setter
    def height(self, val):
        """Set the height of the app"""
        self._height = val

    @property
    def home(self):
        """Return the PID of the home page"""
        return self._home

    @home.setter
    def home(self, val):
        """Set the PID of the home page"""
        self._home = val

    @property
    def scrollbar(self):
        """Return the scrollbar orient"""
        return self._scrollbar

    @scrollbar.setter
    def scrollbar(self, val):
        """
        Set the scrollbar orient. One of:
        - horizontal
        - vertical
        - both
        """
        self._scrollbar = val

    @property
    def theme(self):
        """Return the current theme"""
        return self._theme

    @theme.setter
    def theme(self, val):
        """Set a theme, ie, a themebase.Theme instance"""
        self._theme = val

    @property
    def on_exit(self):
        """Return the on_exit handler"""
        return self._on_exit

    @on_exit.setter
    def on_exit(self, val):
        """Set the on_exit handler. The handler is a function that accepts no argument"""
        self._on_exit = val

    @property
    def opened_page(self):
        """Return the currently opened page"""
        return self._opened_page

    @property
    def pages(self):
        """Return an internal dictionary that contains pages. Keys are pages ids"""
        return self._pages

    @property
    def pyrustic_app(self):
        """Under the hood, Dresscode uses Pyrustic Framework.
        This property returns the instance of pyrustic.app.App"""
        return self._pyrustic_app

    @property
    def main_view(self):
        """Under the hood, Dresscode uses Pyrustic Framework.
        This property returns the main view."""
        return self._main_view

    @property
    def root(self):
        """Return the root Tk object"""
        return self._root

    @property
    def caching(self):
        """Return a boolean to indicate if the caching option is True or False.
        By default, caching is set to False."""
        return self._caching

    @caching.setter
    def caching(self, val):
        """Set True if you want pages to be cached. Cached pages retains their data.
        By default, caching is set to False."""
        self._caching = val

    def add_page(self, page, category=None, indexable=True):
        """ Add a page to the app.
        Parameters
        ==========
            - page: an instance of dresscode.page.Page
            - category: string, the menu category name under
             which the page is indexed
            - indexable: boolean, if False, the page won't be indexed in the menubar
        """
        pid = page.pid
        if not pid:
            pid = self._gen_pid()
            page.pid = pid
        if pid in self._pages:
            message = "Duplicate page id isn't allowed ({})".format(pid)
            raise Error(message)
        self._pages[pid] = page
        self._pids.append(pid)
        if indexable:
            self._main_view.populate_menubar(pid, page, category)
        page.app = self

    def open_page(self, pid):
        """ Open a page specified by its pid"""
        if pid not in self._pages:
            message = "You cannot open a page that you haven't added yet"
            raise Error(message)
        if self._opened_page:
            if self._caching:
                self._opened_page.remove_page_view()
            else:
                self._opened_page.destroy_page_view()
        page = self._pages[pid]
        self._opened_page = page
        scrollbox = self._main_view.body
        #scrollbox.clear()
        page.install_page_view(scrollbox.box)

    def open_home(self):
        """ Open the home page if it's available """
        if self._home:
            self.open_page(self._home)

    def start(self):
        """ Start the app. Mainloop here."""
        self._pyrustic_app.start()

    def _setup(self):
        # set theme
        if self._theme:
            self._pyrustic_app.theme = self._theme
        # set title
        self._pyrustic_app.title = self._title
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


class _MainView(Viewable):

    def __init__(self, app, scrollbar):
        super().__init__()
        self._app = app
        self._scrollbar = scrollbar
        self._root = app.root
        self._body = None
        self._menubar = None
        self._menu_cache = []
        self._menu_map = {}

    def _build(self):
        self._body = Scrollbox(self._root,
                               orient=self._scrollbar)
        # set menubar
        self._menubar = tk.Menu(self._root)
        self._root.config(menu=self._menubar)

    def _on_map(self):
        # consume menu cache
        for pid, page, category in self._menu_cache:
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


class Error(Exception):
    def __init__(self, *args, **kwargs):
        self.code = 0
        self.message = args[0] if args else ""
        super().__init__(self.message)

    def __str__(self):
        return self.message
