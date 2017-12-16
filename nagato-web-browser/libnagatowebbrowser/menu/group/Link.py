
from libnagatowebbrowser.menu.group.Core import NagatoCore


class NagatoLink(NagatoCore):

    def _on_toggle_hide(self, hit_test_result):
        if not hit_test_result.context_is_link():
            self._hide_all()
        else:
            self._last_uri = hit_test_result.get_link_uri()

    def _yuki_n_open_link(self):
        self._raise("YUKI.N > create", self._last_uri)

    def _yuki_n_save_link(self):
        pass

    def _add_menu_items(self):
        self._last_uri = ""
        self._add_menu_item("Open Link in New Tab", "YUKI.N > open link")
        self._add_menu_item("Save Link", "YUKI.N > save link")

