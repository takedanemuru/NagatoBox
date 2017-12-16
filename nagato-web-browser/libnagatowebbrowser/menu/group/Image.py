
from libnagatowebbrowser.menu.group.Core import NagatoCore
from libnagatowebbrowser import DialogFile

class NagatoImage(NagatoCore):

    def _on_toggle_hide(self, hit_test_result):
        if not hit_test_result.context_is_image():
            self._hide_all()
        else:
            self._last_uri = hit_test_result.get_image_uri()

    def _yuki_n_open_image(self):
        self._raise("YUKI.N > create", self._last_uri)

    def _yuki_n_save_image(self):
        DialogFile.save_image_from_uri(self._last_uri)

    def _add_menu_items(self):
        self._last_uri = ""
        self._add_menu_item("Open Image", "YUKI.N > open image")
        self._add_menu_item("Save Image", "YUKI.N > save image")
