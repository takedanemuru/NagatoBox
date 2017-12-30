
from libnagatowebbrowser.menu.action.ActionCore import NagatoActionCore


class NagatoOpenImage(NagatoActionCore):

    def _on_activate(self, widget):
        self._raise(self._message, self._last_url)

    def _on_map(self, widget):
        yuki_hit_test_result = self._enquiry(self._query)
        if not yuki_hit_test_result.context_is_image():
            self.hide()
        else:
            self._last_url = yuki_hit_test_result.get_image_uri()
            self.show()

    def _initialize_variables(self):
        self._title = "Open Image In New Tab"
        self._query = "YUKI.N > hit test result"
        self._message = "YUKI.N > create"
