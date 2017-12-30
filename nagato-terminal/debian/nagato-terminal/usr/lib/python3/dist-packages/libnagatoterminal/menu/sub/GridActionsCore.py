
from gi.repository import Gtk
from libnagato.menu.Item import NagatoItem
from libnagato.flexgrid.Data import NagatoData
from libnagatoterminal.menu.sub.SubCore import NagatoSubCore

MESSAGE = "YUKI.N > menu clicked"


class NagatoGridActionsCore(NagatoSubCore):

    def _get_data(self, gtk_position_type):
        return NagatoData(
                self._enquiry("YUKI.N > notebook itself"),
                gtk_position_type,
                self._enquiry(self._data_query, gtk_position_type)
                )

    def _add_child_menu_item(self, title, gtk_position_type):
        NagatoItem(self, title, MESSAGE, gtk_position_type)

    def _initialize_child_menus(self):
        self._add_child_menu_item("Left", Gtk.PositionType.LEFT)
        self._add_child_menu_item("Bottom", Gtk.PositionType.BOTTOM)
        self._add_child_menu_item("Top", Gtk.PositionType.TOP)
        self._add_child_menu_item("Right", Gtk.PositionType.RIGHT)

    def _set_variables(self):
        self._title = ""
        self._data_query = ""
