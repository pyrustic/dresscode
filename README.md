
<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-animated-logo.gif" alt="Cover">
    <br>
    <p align="center">
    </p>
</div>



<!-- Intro Text -->
# Dresscode
<b> Dress up your code with a beautiful graphical user interface ! </b>

This project is part of the [Pyrustic Ecosystem](https://github.com/pyrustic/pyrustic#overview). Look powered by the [cyberpunk](https://github.com/pyrustic/tk-cyberpunk-theme#readme) theme.

<!-- Quick Links -->
[Showcase](#showcase) | [Installation](#installation) | [Usage](#usage) | [Tutorial](#tutorial) | [Reference](#reference)


# Showcase

Welcome ! Let me show you something:

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-1.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 1 - Demo </b>
    </p>
</div>

What if I told you that I did this with `1 Hex-digit lines of code` :tm: ?

The menu bar in `Figure 1` is not a gimmick. Clicking on the buttons in the menu bar opens another page. So in fact I showed only 1/3 of the pages !

Let's take a look at the other pages:

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-2.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 2 - 1 hex-digit lines of code generated an app with 3 pages ! </b>
    </p>
</div>


Now you are wondering how I did this with just `1 hex-digit lines of code` :tm:.

Well, I first defined the first page:

```python
from dresscode import page

home_page = page.Page(pid="home", name="Home")
home_page.add_entry(title="Username")
home_page.add_entry(title="Password", secretive=True)
home_page.add_button(new_row=True)
```

Then I defined the second page:

```python
from dresscode import page

edit_page = page.Page(pid="edit", name="Edit")
edit_page.add_entry(title="Username")
edit_page.add_button(on_click=lambda page, cid: page.show_toast("Hello"))
```

Then the third page:

```python
from dresscode import page

about_page = page.Page(pid="about", name="About")
about_page.add_button(text="Open Github")
about_page.add_button(text="Download the Wheel")
```


And then I created the app and linked the three pages to it.
```python
from dresscode import app, page
...
my_app = app.App(title="Dresscode Demo", width=450, height=150, home="home")
my_app.add_page(home_page)
my_app.add_page(edit_page)
my_app.add_page(about_page)
my_app.start()
```

The 1 hex-digit lines of code:

```python
from dresscode import app, page
my_app = app.App(title="Dresscode Demo", width=450, height=150, home="home")
home_page = page.Page(pid="home", name="Home")
home_page.add_entry(title="Username")
home_page.add_entry(title="Password", secretive=True)
home_page.add_button(new_row=True)
edit_page = page.Page(pid="edit", name="Edit")
edit_page.add_entry(title="Username")
edit_page.add_button(on_click=lambda page, cid: page.show_toast("Hello"))
about_page = page.Page(pid="about", name="About")
about_page.add_button(text="Open Github")
about_page.add_button(text="Download the Wheel")
my_app.add_page(home_page)
my_app.add_page(edit_page)
my_app.add_page(about_page)
my_app.start()
```



<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-3.gif" alt="Figure" width="650">
    <p align="center">
    <b> Figure 3 - Demo Animation </b>
    </p>
</div>

Voilà !

This is the full source code with comment and well structured:

```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    # defining the home page here
    page = Page(pid="home", name="Home")  # pid = page id !
    page.add_entry(title="Username")
    page.add_entry(title="Password", secretive=True)  # secret secret !
    page.add_button(new_row=True)
    return page


def get_edit_page():
    page = Page(pid="edit", name="Edit")
    page.add_entry(title="Username")
    # Clicking this button will pop up a "Hello"
    page.add_button(on_click=lambda page, cid: page.show_toast("Hello"))
    return page


def get_about_page():
    page = Page(pid="about", name="About")
    page.add_button(text="Open Github")
    page.add_button(text="Download the Wheel")
    return page


# the home argument is the pid of the page to show at start up
app = App(title="Dresscode Demo", width=450, height=150, home="home")

# adding pages to the app !
app.add_page(get_home_page())
app.add_page(get_edit_page())
app.add_page(get_about_page())

# lift up !
app.start()  # the mainloop is hidden here ! ;)

```

Basically, you can just `pip install dresscode`, open a lightweight code editor, copy, paste, run the code and yeah it should work ! Try it !

Wondering what will happen when there are 10 pages ? Yes your menu bar will be full. The solution: buy large screens !

Joking aside, here's the solution:

```python
...
# Asking Dresscode to create a dropdown menu 'Menu'
# then stack inside it the references to the pages ! 
app.add_page(home_page, category="Menu")
app.add_page(edit_page, category="Menu")
app.add_page(about_page, category="Menu")
...

```
<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-4.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 4 - No need to buy large screens ! </b>
    </p>
</div>


## Installation

```bash

pip install dresscode --upgrade --upgrade-strategy eager

```


## Interaction with Dresscode
_Dress up your code with a beautiful graphical user interface !_ was the intro to this README. There is a clear distinction between the backend and the frontend. The question that arises is therefore how to communicate the frontend and the backend.

With `Dresscode`, you can specify when creating a component which handler to call when a particular event occurs.

With the button component, there are the `on_click` parameter to keep a reference to the event handler. So basically, you just need to have a handler with 2 parameters: `page` and `cid`.

```python
from dresscode.app import App
from dresscode.page import Page


def handler(page, cid):
    """
    page: the page object
    cid: the component id (here, the button cid)
    """
    # say 'Hello' !
    page.show_toast("Hello component {}".format(cid))
    # you can inspect the dict of components (keys are cid)
    components = page.components  # be curious, inspect the dict !
    # you can retrieve the data from a component
    username = page.read_component("username")
    # or you can display a large text
    page.show_text("Helloo\n{}".format(username), title="My large text")
    # or, ask for a confirmation
    ok = page.ask_confirmation()  # blocks the app, returns a boolean
    # you can even decide to scroll the content of the page
    page.scroll(value=1.0)
    # you can add a new page at runtime !!!
    app = page.app
    app.add_page(Page(pid="new_page", name="New"))
    # and guess what, you can open this new page !
    app.open_page("new_page")
    # and if you are in a hurry to open the home page
    app.open_home()


def get_home_page():
    # home page - a pid will be generated automatically if you don't set it
    page = Page(pid="home", name="Home")
    page.add_entry(cid="username", title="Username")
    # if you don't set a cid, it will be generated
    page.add_button(on_click=handler)  # a cid will be generated automatically

    # Note, if you click the button twice, you will get a:
    # dresscode.exception.DresscodeException
    # Duplicate page id isn't allowed (new_page) !
    # Guess why ! This isn't a bug but a feature ! hahaha !
    return page


app = App(title="Dresscode Demo", width=450, height=150, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```



## Components

Do you think Dresscode only offers two components, the input field and the button ?

Normally that would be enough. But I implemented a multitude of components to allow everyone to build applications quickly, from the simplest to the most complex.

### Checkbuttons

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-5.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 5 - Checkbuttons </b>
    </p>
</div>

```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    page = Page(pid="home", name="Home")
    items = ("Banana", "Apple", "Avocado")
    page.add_checkbutton(title="Choose your favorite fruits", items=items)
    # you could add a on_choice event handler ;)
    return page


app = App(title="Dresscode Demo", width=450, height=150, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```

### Dropdown list

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-6.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 6 - Drop-down list </b>
    </p>
</div>

```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    page = Page(pid="home", name="Home")
    items = ("Banana", "Apple", "Avocado")
    page.add_dropdown_list(title="Choose your favorite fruit", items=items)
    # you could add a on_choice event handler ;)
    return page


app = App(title="Dresscode Demo", width=450, height=150, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```

### Editor

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-7.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 7 - Editor </b>
    </p>
</div>

```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    page = Page(pid="home", name="Home")
    essay = "non est ad astra mollis e terris via\nSénèque"
    page.add_editor(title="My essay", text=essay, readonly=True)
    # you could change the width and or height...
    return page


app = App(title="Dresscode Demo", width=450, height=150, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```

### Label

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-8.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 8 - Label </b>
    </p>
</div>

```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    page = Page(pid="home", name="Home")
    page.add_label(text="Marvelous")
    page.add_label(text="Dresscode", color="white")
    page.add_label(text="Project", color="cyan")
    text = "Make Desktop Apps Great Again !"
    page.add_label(new_row=True, text=text, color="gray",
                   side="right",
                   font=("Corrier", 10))
    return page


app = App(title="Dresscode Demo", width=450, height=150, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```

### Radiobuttons

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-9.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 9 - Radiobuttons </b>
    </p>
</div>

```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    page = Page(pid="home", name="Home")
    items = ("Blue", "Red")
    page.add_radiobutton(title="Make a choice", items=items)

    return page


app = App(title="Dresscode Demo", width=450, height=150, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```

### Space

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-10.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 10 - SpaceX </b>
    </p>
</div>

```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    page = Page(pid="home", name="Home")
    items = ("Blue", "Red")
    page.add_button()
    page.add_button()
    page.add_space()  # you can alter the width, height and more...
    page.add_button()

    return page


app = App(title="Dresscode Demo", width=450, height=150, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```

### Spinbox

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-11.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 11 - Spinbox </b>
    </p>
</div>

```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    page = Page(pid="home", name="Home")
    items = ("Blue", "Red")
    page.add_spinbox(title="Make a choice", items=items)
    return page


app = App(title="Dresscode Demo", width=450, height=150, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```


### path entry
The path entry is part of `pyrustic.widget`. Discover the [Pyrustic framework](https://github.com/pyrustic/pyrustic/#readme) !

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-12.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 12 - Pathentry </b>
    </p>
</div>

```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    page = Page(pid="home", name="Home")
    page.add_path_entry(title="Directory", browse="dir")
    page.add_path_entry(new_row=True, title="File")
    return page


app = App(title="Dresscode Demo", width=450, height=150, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```

### Table
The table is part of `pyrustic.widget`. Discover the [Pyrustic framework](https://github.com/pyrustic/pyrustic/#readme) !

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-13.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 13 - Table </b>
    </p>
</div>

```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    page = Page(pid="home", name="Home")
    columns = ("Name", "Age", "Gender")
    data = [("Jack", 45, "Male"), ("Jane", 37, "Female"), ("Alex", 100, "?")]
    page.add_table(title="My data", columns=columns, data=data)
    return page


app = App(title="Dresscode Demo", width=650, height=300, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```

### Image
Admit that you didn't expect this !

<!-- Image -->
<div align="center">
    <img src="https://raw.githubusercontent.com/pyrustic/misc/master/media/dresscode-figure-14.png" alt="Figure" width="650">
    <p align="center">
    <b> Figure 14 - Image </b>
    </p>
</div>


```python
from dresscode.app import App
from dresscode.page import Page


def get_home_page():
    page = Page(pid="home", name="Home")
    page.add_label(text="Welcome !", side=None, anchor="center", color="gray")
    with open("/home/alex/dresscode.png", "rb") as file:
        image = file.read()
    # to center any component, the trick: side=None, anchor="center" !
    page.add_image(new_row=True, image=image, side=None, anchor="center")
    page.add_label(text="https://github.com/pyrustic", side=None, anchor="center",
                   font=("Courrier", 10), new_row=True, color="gray")
    return page


app = App(title="Dresscode Demo", width=650, height=400, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```

### Cherry on the cake

Since we have this rebellious little side to wanting to customize everything, I implemented the possibility of adding custom components !

```python
from dresscode.app import App
from dresscode.page import Page


# I will cover this topic another time !


def data_getter(page, cid):
    data = None
    return data


def builder(page, cid):
    parts = {}
    return parts, data_getter


def get_home_page():
    page = Page(pid="home", name="Home")
    page.add_custom(builder=builder)
    return page


app = App(title="Dresscode Demo", width=650, height=400, home="home")

app.add_page(get_home_page())

# lift up !
app.start()

```

There you go, so I won't be asked to add new components ! :)

## Epilog

I created a Discord for announcements and discussions etc. Join the [Discord](https://discord.gg/fSZ6nxzVd6) !


Work in progress...
