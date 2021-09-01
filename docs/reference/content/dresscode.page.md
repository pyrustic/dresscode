
Back to [Reference Overview](https://github.com/pyrustic/dresscode/blob/master/docs/reference/README.md#readme)

# dresscode.page



<br>


```python
COMPONENT_BUILDER = {'space': <function builder at 0x7f4ad45220d0>, 'label': <function builder at 0x7f4ad451a0d0>, 'entry': <function builder at 0x7f4ad4513af0>, 'button': <function builder at 0x7f4ad4513040>, 'editor': <function builder at 0x7f4ad4513820>, 'checkbutton': <function builder at 0x7f4ad4513310>, 'radiobutton': <function builder at 0x7f4ad451adc0>, 'spinbox': <function builder at 0x7f4ad4522430>, 'dropdown_list': <function builder at 0x7f4ad45135e0>, 'path_entry': <function builder at 0x7f4ad451a3a0>, 'image': <function builder at 0x7f4ad4513e50>, 'table': <function builder at 0x7f4ad4522700>}

COMPONENT_READER = {'space': <function reader at 0x7f4ad4522280>, 'label': <function reader at 0x7f4ad451a1f0>, 'entry': <function reader at 0x7f4ad4513ca0>, 'button': <function reader at 0x7f4ad4513160>, 'editor': <function reader at 0x7f4ad4513940>, 'checkbutton': <function reader at 0x7f4ad4513430>, 'radiobutton': <function reader at 0x7f4ad451aee0>, 'spinbox': <function reader at 0x7f4ad4522550>, 'dropdown_list': <function reader at 0x7f4ad4513670>, 'path_entry': <function reader at 0x7f4ad451a550>, 'image': <function reader at 0x7f4ad4513ee0>, 'table': <function reader at 0x7f4ad4524b80>}

COMPONENT_UPDATER = {'space': <function updater at 0x7f4ad4522310>, 'label': <function updater at 0x7f4ad451a280>, 'entry': <function updater at 0x7f4ad4513d30>, 'button': <function updater at 0x7f4ad45131f0>, 'editor': <function updater at 0x7f4ad45139d0>, 'checkbutton': <function updater at 0x7f4ad45134c0>, 'radiobutton': <function updater at 0x7f4ad451af70>, 'spinbox': <function updater at 0x7f4ad45225e0>, 'dropdown_list': <function updater at 0x7f4ad4513700>, 'path_entry': <function updater at 0x7f4ad451aca0>, 'image': <function updater at 0x7f4ad4513f70>, 'table': <function updater at 0x7f4ad4524d30>}

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

