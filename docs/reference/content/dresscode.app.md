
Back to [Reference Overview](https://github.com/pyrustic/dresscode/blob/master/docs/reference/README.md)

# dresscode.app



<br>


```python

class App:
    """
    This is the entry point of your Dresscode app
    """

    def __init__(self, title=None, width=900, height=550, home=None, scrollbar='vertical', theme=<cyberpunk_theme.Cyberpunk object at 0x7fed2e561a60>, on_exit=None):
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

    @property
    def caching(self):
        """
        Return a boolean to indicate if the caching option is True or False.
        By default, caching is set to False.
        """

    @caching.setter
    def caching(self, val):
        """
        Set True if you want pages to be cached. Cached pages retains their data.
        By default, caching is set to False.
        """

    @property
    def height(self):
        """
        Return the height of the app
        """

    @height.setter
    def height(self, val):
        """
        Set the height of the app
        """

    @property
    def home(self):
        """
        Return the PID of the home page
        """

    @home.setter
    def home(self, val):
        """
        Set the PID of the home page
        """

    @property
    def main_view(self):
        """
        Under the hood, Dresscode uses Pyrustic Framework.
        This property returns the main view.
        """

    @property
    def on_exit(self):
        """
        Return the on_exit handler
        """

    @on_exit.setter
    def on_exit(self, val):
        """
        Set the on_exit handler. The handler is a function that accepts no argument
        """

    @property
    def opened_page(self):
        """
        Return the currently opened page
        """

    @property
    def pages(self):
        """
        Return an internal dictionary that contains pages. Keys are pages ids
        """

    @property
    def pyrustic_app(self):
        """
        Under the hood, Dresscode uses Pyrustic Framework.
        This property returns the instance of pyrustic.app.App
        """

    @property
    def root(self):
        """
        Return the root Tk object
        """

    @property
    def scrollbar(self):
        """
        Return the scrollbar orient
        """

    @scrollbar.setter
    def scrollbar(self, val):
        """
        Set the scrollbar orient. One of:
        - horizontal
        - vertical
        - both
        """

    @property
    def theme(self):
        """
        Return the current theme
        """

    @theme.setter
    def theme(self, val):
        """
        Set a theme, ie, a themebase.Theme instance
        """

    @property
    def title(self):
        """
        Return the title of the app
        """

    @title.setter
    def title(self, val):
        """
        Set the title of the app
        """

    @property
    def width(self):
        """
        Return the width of the app
        """

    @width.setter
    def width(self, val):
        """
        Set the width of the app
        """

    def add_page(self, page, category=None, indexable=True):
        """
        Add a page to the app.
        Parameters
        ==========
            - page: an instance of dresscode.page.Page
            - category: string, the menu category name under
             which the page is indexed
            - indexable: boolean, if False, the page won't be indexed in the menubar
        """

    def open_home(self):
        """
        Open the home page if it's available 
        """

    def open_page(self, pid):
        """
        Open a page specified by its pid
        """

    def start(self):
        """
        Start the app. Mainloop here.
        """

```

<br>

```python

class Error:
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

```

