
from libnagatowebbrowser import DialogFile
from libnagatowebbrowser.menu.action.ActionCore import NagatoActionCore


class NagatoSaveImage(NagatoActionCore):

    def _on_activate(self, widget):
        DialogFile.save_image_from_uri(self._last_uri)

    def _on_map(self, widget):
        yuki_hit_test_result = self._enquiry(self._query)
        if yuki_hit_test_result.context_is_image():
            self._last_uri = yuki_hit_test_result.get_image_uri()
            self.show()
        else:
            self.hide()

    def _initialize_variables(self):
        self._title = "Save Image"
        self._query = "YUKI.N > hit test result"
        self._message = ""
