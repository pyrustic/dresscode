from dresscode.component import button
from dresscode.component import checkbutton
from dresscode.component import dropdown_list
from dresscode.component import editor
from dresscode.component import entry
from dresscode.component import image
from dresscode.component import label
from dresscode.component import path_entry
from dresscode.component import radiobutton
from dresscode.component import space
from dresscode.component import spinbox
from dresscode.component import table


COMPONENT_BUILDER = \
    {
        "space": space.builder,
        "label": label.builder,
        "entry": entry.builder,
        "button": button.builder,
        "editor": editor.builder,
        "checkbutton": checkbutton.builder,
        "radiobutton": radiobutton.builder,
        "spinbox": spinbox.builder,
        "dropdown_list": dropdown_list.builder,
        "path_entry": path_entry.builder,
        "image": image.builder,
        "table": table.builder
    }
