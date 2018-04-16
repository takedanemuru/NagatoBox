
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoSubCore(Gtk.Menu, NagatoObject):

    def _on_map(self, widget):
        pass

    def _initialize_root_menu_item(self):
        Gtk.Menu.__init__(self)
        self._root_menu_item = Gtk.MenuItem(self._title)
        self._root_menu_item.set_submenu(self)
        self._root_menu_item.connect("map", self._on_map)
        self._parent.append(self._root_menu_item)

    def _initialize_child_menus(self):
        pass

    def _set_variables(self):
        self._title = ""
        self._data_query = ""

    def __init__(self, parent):
        self._parent = parent
        self._set_variables()
        self._initialize_root_menu_item()
        self._initialize_child_menus()
