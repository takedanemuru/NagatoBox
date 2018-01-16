
from libnagato.menu.Item import NagatoItem
from libnagatowebbrowser.menu.sub.SubCore import NagatoSubCore
from libnagatowebbrowser.menu.sub.SearchWeb import NagatoSearchWeb
from libnagatowebbrowser.menu.sub.SearchMisc import NagatoSearchMisc


class NagatoSearchSelection(NagatoSubCore):

    def _on_map(self, widget):
        yuki_hit_test_result = self._enquiry(self._data_query)
        if not yuki_hit_test_result.context_is_selection():
            self._root_menu_item.hide()
        else:
            self._root_menu_item.show()

    def _initialize_child_menus(self):
        NagatoSearchWeb(self)
        NagatoSearchMisc(self)

    def _set_variables(self):
        self._title = "Search"
        self._data_query = "YUKI.N > hit test result"
