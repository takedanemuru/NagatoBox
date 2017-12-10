
from libnagatoterminal.SubMenuGridAction import NagatoSubMenuGridAction


class NagatoSubMenuNew(NagatoSubMenuGridAction):

    def _yuki_n_menu_clicked(self, gtk_position_type):
        self._raise("YUKI.N > new vte to", self._get_data(gtk_position_type))

    def _set_variables(self):
        self._title = "New VTE"
        self._data_query = "YUKI.N > new vte rect"
