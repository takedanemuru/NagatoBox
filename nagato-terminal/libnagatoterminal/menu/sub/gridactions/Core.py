
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatoterminal.menu.Item import NagatoItem
from libnagato.flexgrid.Data import NagatoData

MESSAGE = "YUKI.N > menu clicked"


class NagatoCore(Gtk.Menu, NagatoObject):

    def _get_data(self, gtk_position_type):
        return NagatoData(
                self._enquiry("YUKI.N > notebook itself"),
                gtk_position_type,
                self._enquiry(self._data_query, gtk_position_type)
                )

    def _add_child_menu_item(self, title, gtk_position_type):
        NagatoItem(self, title, MESSAGE, gtk_position_type)

    def _on_map(self, widget):
        pass

    def _initialize_root_menu_item(self):
        Gtk.Menu.__init__(self)
        self._root_menu_item = Gtk.MenuItem(self._title)
        self._root_menu_item.set_submenu(self)
        self._root_menu_item.connect("map", self._on_map)
        self._parent.append(self._root_menu_item)

    def _initialize_child_menus(self):
        self._add_child_menu_item("Left", Gtk.PositionType.LEFT)
        self._add_child_menu_item("Bottom", Gtk.PositionType.BOTTOM)
        self._add_child_menu_item("Top", Gtk.PositionType.TOP)
        self._add_child_menu_item("Right", Gtk.PositionType.RIGHT)

    def _set_variables(self):
        self._title = ""
        self._data_query = ""

    def __init__(self, parent):
        self._parent = parent
        self._set_variables()
        self._initialize_root_menu_item()
        self._initialize_child_menus()
