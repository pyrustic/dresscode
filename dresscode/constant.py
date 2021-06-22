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

COMPONENT_READER = \
    {
        "space": space.reader,
        "label": label.reader,
        "entry": entry.reader,
        "button": button.reader,
        "editor": editor.reader,
        "checkbutton": checkbutton.reader,
        "radiobutton": radiobutton.reader,
        "spinbox": spinbox.reader,
        "dropdown_list": dropdown_list.reader,
        "path_entry": path_entry.reader,
        "image": image.reader,
        "table": table.reader
    }


COMPONENT_UPDATER = \
    {
        "space": space.updater,
        "label": label.updater,
        "entry": entry.updater,
        "button": button.updater,
        "editor": editor.updater,
        "checkbutton": checkbutton.updater,
        "radiobutton": radiobutton.updater,
        "spinbox": spinbox.updater,
        "dropdown_list": dropdown_list.updater,
        "path_entry": path_entry.updater,
        "image": image.updater,
        "table": table.updater
    }
