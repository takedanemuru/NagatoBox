
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatoterminal.menu.Item import NagatoItem
from libnagatoterminal.datatype.GridData import NagatoGridData

MESSAGE = "YUKI.N > menu clicked"


class NagatoCore(Gtk.Menu, NagatoObject):

    def _get_data(self, gtk_position_type):
        return NagatoGridData(
                self._enquiry("YUKI.N > notebook itself"),
                gtk_position_type,
                self._enquiry(self._data_query, gtk_position_type)
                )

    def _add_child_menu_item(self, title, gtk_position_type):
        NagatoItem(self, title, MESSAGE, gtk_position_type)

    def _initialize_root_menu_item(self):
        Gtk.Menu.__init__(self)
        yuki_root_menu_item = Gtk.MenuItem(self._title)
        yuki_root_menu_item.set_submenu(self)
        self._parent.append(yuki_root_menu_item)

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
