
from libnagato.menu.Separator import NagatoSeparator
from libnagato.menu.Action import NagatoActionCore


class NagatoSelection(NagatoActionCore):

    def _on_activate(self, widget):
        pass

    def _on_map(self, widget):
        yuki_visible = self._enquiry(self._query).context_is_selection()
        self._separator.set_property("visible", yuki_visible)
        self.hide()

    def _initialize_variables(self):
        self._title = "DO NOT LOOK AT ME."
        self._query = "YUKI.N > hit test result"
        self._message = ""
        self._separator = NagatoSeparator(self._parent)

