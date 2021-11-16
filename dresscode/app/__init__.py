import tkinter as tk
from viewable import Viewable
from pyrustic.app import App as PyrusticApp
from cyberpunk_theme import Cyberpunk
from megawidget import ScrollBox
from dresscode import error


class App:
    """This is the entry point of your Dresscode app"""
    def __init__(self, title="Dresscode App", width=800, height=500,
                 theme=Cyberpunk(), caching=False,
                 resizable=(False, True), on_exit=None):
        """
        Parameters
        ==========
        - title: string, the title of the app
        - width: int, the width of the app
        - height: int, the height of the app
        - scrolling: the orient of the scrollbar, "vertical", "horizontal", "both".
        - theme: the theme, i.e. an instance of tkstyle.Theme
        - on_exit: the on_exit handler, ie a function that will be called on exit.
        """
        self._title = title
        self._width = width
        self._height = height
        self._theme = theme
        self._caching = caching
        self._resizable = resizable
        self._on_exit = on_exit
        self._pages = {}
        self._page = None
        self._todo_open_cache = []
        self._todo_menu_cache = []
        self._menubar = None
        self._view = None
        self._menu_map = {}
        self._pids = []
        self._pids_count = 0
        self._pyrustic_app = PyrusticApp()
        self._root = self._pyrustic_app.root
        self._opening = False
        self._started = False
        self._setup()

    @property
    def title(self):
        """Return the title of the app"""
        return self._title

    @title.setter
    def title(self, val):
        """Set the title of the app"""
        if self._started and self._title:
            raise error.AlreadyDefinedError
        self._title = val

    @property
    def width(self):
        """Return the width of the app"""
        return self._width

    @width.setter
    def width(self, val):
        """Set the width of the app"""
        if self._started and self._width:
            raise error.AlreadyDefinedError
        self._width = val

    @property
    def height(self):
        """Return the height of the app"""
        return self._height

    @height.setter
    def height(self, val):
        """Set the height of the app"""
        if self._started and self._height:
            raise error.AlreadyDefinedError
        self._height = val

    @property
    def theme(self):
        """Return the current theme"""
        return self._theme

    @theme.setter
    def theme(self, val):
        """Set a theme, ie, a themebase.Theme instance"""
        if self._started and self._theme:
            raise error.AlreadyDefinedError
        self._theme = val

    @property
    def caching(self):
        """Return a boolean to indicate if the caching option is True or False.
        By default, caching is set to False."""
        return self._caching

    @caching.setter
    def caching(self, val):
        """Set True if you want pages to be cached. Cached pages retains their data.
        By default, caching is set to False."""
        if self._started and self._caching:
            raise error.AlreadyDefinedError
        self._caching = val

    @property
    def resizable(self):
        """Return the resizable tuple state"""
        return self._pyrustic_app.resizable

    @resizable.setter
    def resizable(self, val):
        if self._started:
            raise error.AlreadyDefinedError
        self._pyrustic_app.resizable = val

    @property
    def on_exit(self):
        """Return the on_exit handler"""
        return self._on_exit

    @on_exit.setter
    def on_exit(self, val):
        """Set the on_exit handler. The handler is a function that accepts no argument"""
        if self._started and self._on_exit:
            raise error.AlreadyDefinedError
        self._on_exit = val

    @property
    def page(self):
        """Return the currently opened page"""
        return self._page

    @property
    def pages(self):
        """Return an internal dictionary that contains pages. Keys are pages ids"""
        return self._pages.copy()

    @property
    def pyrustic_app(self):
        """Under the hood, Dresscode uses Pyrustic Framework.
        This property returns the instance of pyrustic.app.App"""
        return self._pyrustic_app

    @property
    def root(self):
        """Return the root Tk object"""
        return self._root

    @property
    def view(self):
        """Under the hood, Dresscode uses Pyrustic Framework.
        This property returns the main view."""
        return self._view

    def add(self, page, indexable=True, category=None):
        """ Add a page to the app.
        Parameters
        ==========
            - page: an instance of dresscode.page.Page
            - indexable: boolean, if False, the page won't be indexed in the menubar
            - category: string, the menu category name under
             which the page is indexed

        Returns the pid

        Raises dresscode.error.DuplicatePageError if the pid already exists
        """
        if not page.app:
            page.app = self
        if not page.pid:
            page.pid = self.new_pid()
        pid = page.pid
        if pid in self._pages:
            raise error.DuplicatePageError
        self._pages[pid] = page
        self._pids.append(pid)
        if indexable:
            if self._view.body:
                self._view.populate_menubar(pid, page, category)
            else:
                data = (pid, page, category)
                self._todo_menu_cache.append(data)
        return pid

    def new_pid(self):
        self._pids_count += 1
        return "pid-{}".format(self._pids_count)

    def open(self, pid):
        """ Open a page specified by its pid
        Raise dresscode.error.PageNotFoundError if not page is associated to this PID
        Raise dresscode.error.NestedOpeningError if you try to open a new page inside
        on_open and on_close callbacks
        """
        if self._opening:
            msg = "Don't open a new page inside on_open and on_close callbacks"
            raise error.NestedOpeningError(msg)
        if not self._view.body:
            self._todo_open_cache.append(pid)
            return
        if pid not in self._pages:
            raise error.PageNotFoundError
        self._opening = True
        if self._page:
            self._page.close()
        self._page = self._pages[pid]
        self._page.open()
        self._opening = False

    def start(self):
        """ Start the app. Mainloop here."""
        self._started = True
        self._pyrustic_app.start()

    def exit(self):
        """Exit the app"""
        self._pyrustic_app.exit()

    def _setup(self):
        # set theme
        if self._theme:
            self._pyrustic_app.theme = self._theme
        # set title
        self._pyrustic_app.title = self._title
        # set width and height
        if self._width and self._height:
            cache = "{}x{}+0+0".format(self._width, self._height)
            self._root.geometry(cache)
        # set resizable
        self.resizable = self._resizable
        # center the app
        self._pyrustic_app.center()
        # set the main view
        self._view = View(self, self._todo, self._on_exit)
        self._pyrustic_app.view = self._view

    def _todo(self):
        for pid, page, category in self._todo_menu_cache:
            self._view.populate_menubar(pid, page, category)
        for pid in self._todo_open_cache:
            self.open(pid)
        self._todo_menu_cache = []
        self._todo_open_cache = []


class View(Viewable):

    def __init__(self, app, todo_on_map, on_exit):
        super().__init__()
        self._app = app
        self._todo_on_map = todo_on_map
        self._on_exit = on_exit
        self._on_exit = on_exit
        self._root = app.root
        self._body = None
        self._menubar = None
        self._menu_cache = []
        self._menu_map = {}

    def _build(self):
        self._body = tk.Frame(self._root)
        # set menubar
        self._menubar = tk.Menu(self._root)
        self._root.config(menu=self._menubar)

    def _on_map(self):
        self._todo_on_map()

    def populate_menubar(self, pid, page, category):
        page_name = page.name
        command = (lambda self=self, pid=pid:
                   self._app.open(pid))
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

    def _on_destroy(self):
        if self._on_exit:
            self._on_exit()
