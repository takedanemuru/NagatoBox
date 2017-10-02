
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.MenuItem import NagatoMenuItem


class NagatoSubMenuVte(Gtk.Menu, NagatoObject):

    def _add_child_menu_item(self, title, user_data):
        NagatoMenuItem(self, title, self._message, user_data)

    def _initialize_root_menu_item(self):
        Gtk.Menu.__init__(self)
        yuki_root_menu_item = Gtk.MenuItem(self._title)
        yuki_root_menu_item.set_submenu(self)
        self._parent.append(yuki_root_menu_item)

    def _set_variables(self):
        self._message = ""
        self._title = ""

    def __init__(self, parent):
        self._parent = parent
        self._set_variables()
        self._initialize_root_menu_item()
        self._add_child_menu_item("Left", Gtk.PositionType.LEFT)
        self._add_child_menu_item("Bottom", Gtk.PositionType.BOTTOM)
        self._add_child_menu_item("Top", Gtk.PositionType.TOP)
        self._add_child_menu_item("Right", Gtk.PositionType.RIGHT)
