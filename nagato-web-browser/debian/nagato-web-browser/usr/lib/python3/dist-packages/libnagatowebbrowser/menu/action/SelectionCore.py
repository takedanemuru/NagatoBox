
from libnagato.menu.Action import NagatoActionCore


class NagatoSelectionCore(NagatoActionCore):

    def _on_activate(self, widget):
        pass

    def _on_map(self, widget):
        yuki_hit_test_result = self._enquiry(self._query)
        if not yuki_hit_test_result.context_is_selection():
            self.hide()
        else:
            self.show()
