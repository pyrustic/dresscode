
Back to [Reference Overview](https://github.com/pyrustic/dresscode/blob/master/docs/reference/README.md#readme)

# dresscode.page



<br>


```python
COMPONENT_BUILDER = {'space': <function builder at 0x7f5900c09e50>, 'label': <function builder at 0x7f5900c01e50>, 'entry': <function builder at 0x7f5900c018b0>, 'button': <function builder at 0x7f5900bf9dc0>, 'editor': <function builder at 0x7f5900c015e0>, 'checkbutton': <function builder at 0x7f5900c010d0>, 'radiobutton': <function builder at 0x7f5900c09b80>, 'spinbox': <function builder at 0x7f5900c0e1f0>, 'dropdown_list': <function builder at 0x7f5900c013a0>, 'path_entry': <function builder at 0x7f5900c09160>, 'image': <function builder at 0x7f5900c01c10>, 'table': <function builder at 0x7f5900c0e4c0>}

COMPONENT_READER = {'space': <function reader at 0x7f5900c0e040>, 'label': <function reader at 0x7f5900c01f70>, 'entry': <function reader at 0x7f5900c01a60>, 'button': <function reader at 0x7f5900bf9ee0>, 'editor': <function reader at 0x7f5900c01700>, 'checkbutton': <function reader at 0x7f5900c011f0>, 'radiobutton': <function reader at 0x7f5900c09ca0>, 'spinbox': <function reader at 0x7f5900c0e310>, 'dropdown_list': <function reader at 0x7f5900c01430>, 'path_entry': <function reader at 0x7f5900c09310>, 'image': <function reader at 0x7f5900c01ca0>, 'table': <function reader at 0x7f5900ba5940>}

COMPONENT_UPDATER = {'space': <function updater at 0x7f5900c0e0d0>, 'label': <function updater at 0x7f5900c09040>, 'entry': <function updater at 0x7f5900c01af0>, 'button': <function updater at 0x7f5900bf9f70>, 'editor': <function updater at 0x7f5900c01790>, 'checkbutton': <function updater at 0x7f5900c01280>, 'radiobutton': <function updater at 0x7f5900c09d30>, 'spinbox': <function updater at 0x7f5900c0e3a0>, 'dropdown_list': <function updater at 0x7f5900c014c0>, 'path_entry': <function updater at 0x7f5900c09a60>, 'image': <function updater at 0x7f5900c01d30>, 'table': <function updater at 0x7f5900ba5af0>}

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

<br>

```python

class MissingBackendError:
    """
    Common base class for all non-exit exceptions.
    """

```

<br>

```python

class MissingBuilderError:
    """
    Common base class for all non-exit exceptions.
    """

```

<br>

```python

class MissingReaderError:
    """
    Common base class for all non-exit exceptions.
    """

```

<br>

```python

class MissingUpdaterError:
    """
    Common base class for all non-exit exceptions.
    """

```

<br>

```python

class Page:
    """
    
    """

    def __init__(self, pid=None, name='Page', on_open=None, on_close=None, padx=5, pady=5):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    @property
    def app(self):
        """
        Returns the app reference
        """

    @app.setter
    def app(self, val):
        """
        Set the app reference. You aren't supposed to use this property.
        When you add a page to the app instance, the app instance will use
        this property to set its reference.
        """

    @property
    def components(self):
        """
        Returns the dictionary of components if it's available, else returns None.
        The dictionary keys are CIDs (component id)
        """

    @property
    def name(self):
        """
        Returns the page name
        """

    @property
    def page_view(self):
        """
        Returns the page view
        """

    @property
    def pid(self):
        """
        Returns the page id
        """

    @pid.setter
    def pid(self, val):
        """
        Set the page id (string)
        """

    @property
    def root(self):
        """
        Returns the root Tk object if it's available, else returns None
        """

    def add_button(self, cid=None, new_row=False, text='Submit', on_click=None, side='left', anchor='s', style=None):
        """
        
        """

    def add_checkbutton(self, cid=None, new_row=False, title=None, items=None, default=None, stacking='horizontal', on_choice=None, side='left', anchor='s'):
        """
        
        """

    def add_custom(self, cid=None, new_row=False, backend=None, **config):
        """
        backend: a dict with keys: name, builder, reader, updater
                
        """

    def add_dropdown_list(self, cid=None, new_row=False, title=None, items=None, default=None, prompt='- Select -', on_choice=None, side='left', anchor='s'):
        """
        
        """

    def add_editor(self, cid=None, new_row=False, title=None, text=None, readonly=False, width=45, height=10, fill_row=False, side='left', anchor='s'):
        """
        
        """

    def add_entry(self, cid=None, new_row=False, title=None, text=None, width=20, secretive=False, on_submit=None, side='left', anchor='s'):
        """
        
        """

    def add_image(self, cid=None, new_row=False, title=None, image=None, width=0, height=0, on_click=None, side='left', anchor='s'):
        """
        
        """

    def add_label(self, cid=None, new_row=False, text='Text', color='tomato', font=('Courrier', 20), side='left', anchor='n'):
        """
        
        """

    def add_path_entry(self, cid=None, new_row=False, title=None, text=None, browse='file', width=17, on_submit=None, side='left', anchor='s'):
        """
        
        """

    def add_radiobutton(self, cid=None, title=None, items=None, default=None, stacking='horizontal', new_row=False, side='left', anchor='s', on_choice=None):
        """
        
        """

    def add_space(self, cid=None, new_row=False, width=20, height=20, side='left', anchor='center'):
        """
        
        """

    def add_spinbox(self, cid=None, new_row=False, title=None, items=None, default=None, prompt='- Select -', on_submit=None, side='left', anchor='s'):
        """
        
        """

    def add_table(self, cid=None, new_row=False, title=None, columns=None, data=None, on_click=None, side='left', anchor='s'):
        """
        
        """

    def ask_confirmation(self, title='Confirmation', message='Attention required.\nDo you want to continue ?'):
        """
        Displays a confirmation dialog. Returns a boolean
        """

    def destroy_page_view(self):
        """
        
        """

    def install_page_view(self, master):
        """
        
        """

    def read_component(self, cid):
        """
        Returns the content of a component. Each component has
        a reader function that is invoked with the cid as argument.
        The returned value of the reader function is the one returned
        by the method read_component()
        """

    def remove_component(self, cid):
        """
        
        """

    def remove_page_view(self):
        """
        
        """

    def scroll(self, orient='y', value=1):
        """
        Scrolls the page
        For orient = x:
            - 0: to scroll to left
            - 1: to scroll to right
        For orient = y:
            - 0: to scroll to top
            - 1: to scroll to bottom
        """

    def show_text(self, message, title='Text', width=60, height=22):
        """
        Displays a text
        """

    def show_toast(self, message, duration=1000):
        """
        Displays a toast that will last for x milliseconds (duration)
        """

    def update_component(self, cid, **config):
        """
        
        """

```

