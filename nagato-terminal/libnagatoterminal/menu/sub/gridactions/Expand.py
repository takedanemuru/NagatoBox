
from libnagatoterminal.menu.sub.gridactions.Core import NagatoCore


class NagatoExpand(NagatoCore):

    def _yuki_n_menu_clicked(self, gtk_position_type):
        self._raise("YUKI.N > expand to", self._get_data(gtk_position_type))

    def _on_map(self, widget):
        yuki_number = self._enquiry("YUKI.N > number of grid children")
        self._root_menu_item.set_sensitive(yuki_number > 1)

    def _set_variables(self):
        self._title = "Expand VTE to..."
        self._data_query = "YUKI.N > expanded rect"
