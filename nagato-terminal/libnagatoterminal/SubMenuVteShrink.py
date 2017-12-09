
from gi.repository import Gtk
from libnagatoterminal.SubMenuVte import NagatoSubMenuVte
from libnagatoterminal.MenuItemVteShrink import NagatoMenuItemVteShrink


class NagatoSubMenuVteShrink(NagatoSubMenuVte):

    def _yuki_n_menu_clicked(self, gtk_position_type):
        if self._enquiry("YUKI.N > can shrink to", gtk_position_type):
            self._raise("YUKI.N > shrink to",self._get_data(gtk_position_type))

    def _initialize_child_menus(self):
        NagatoMenuItemVteShrink(self, "Left", Gtk.PositionType.LEFT)
        NagatoMenuItemVteShrink(self, "Top", Gtk.PositionType.TOP)
        NagatoMenuItemVteShrink(self, "Bottom", Gtk.PositionType.BOTTOM)
        NagatoMenuItemVteShrink(self, "Right", Gtk.PositionType.RIGHT)

    def _set_variables(self):
        self._title = "Shrink VTE to..."
        self._data_query = "YUKI.N > shrinked rect"
