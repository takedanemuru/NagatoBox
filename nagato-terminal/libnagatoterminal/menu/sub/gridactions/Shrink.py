
from gi.repository import Gtk
from libnagatoterminal.menu.sub.gridactions.Core import NagatoCore
from libnagatoterminal.menu.item.sensitive.Shrink import (
    NagatoShrink as NagatoShrinkMenuItem
    )

class NagatoShrink(NagatoCore):

    def _yuki_n_menu_clicked(self, gtk_position_type):
        self._raise("YUKI.N > shrink to", self._get_data(gtk_position_type))

    def _initialize_child_menus(self):
        NagatoShrinkMenuItem(self, "Left", Gtk.PositionType.LEFT)
        NagatoShrinkMenuItem(self, "Top", Gtk.PositionType.TOP)
        NagatoShrinkMenuItem(self, "Bottom", Gtk.PositionType.BOTTOM)
        NagatoShrinkMenuItem(self, "Right", Gtk.PositionType.RIGHT)

    def _on_map(self, widget):
        yuki_sensitive = self._enquiry("YUKI.N > can shrink")
        self._root_menu_item.set_sensitive(yuki_sensitive)

    def _set_variables(self):
        self._title = "Shrink VTE to..."
        self._data_query = "YUKI.N > shrinked rect"
