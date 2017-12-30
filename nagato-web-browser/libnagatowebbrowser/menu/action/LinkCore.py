
from libnagatowebbrowser.menu.action.ActionCore import NagatoActionCore


class NagatoLinkCore(NagatoActionCore):

    def _on_activate(self, widget):
        pass

    def _on_map(self, widget):
        yuki_hit_test_result = self._enquiry(self._query)
        if not yuki_hit_test_result.context_is_link():
            self.hide()
        else:
            self._last_url = yuki_hit_test_result.get_link_uri()
            self.show()
