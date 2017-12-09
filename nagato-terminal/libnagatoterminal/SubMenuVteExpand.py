
from libnagatoterminal.SubMenuVte import NagatoSubMenuVte


class NagatoSubMenuVteExpand(NagatoSubMenuVte):

    def _yuki_n_menu_clicked(self, gtk_position_type):
        self._raise("YUKI.N > expand to", self._get_data(gtk_position_type))

    def _set_variables(self):
        self._title = "Expand VTE to..."
        self._data_query = "YUKI.N > expanded rect"
