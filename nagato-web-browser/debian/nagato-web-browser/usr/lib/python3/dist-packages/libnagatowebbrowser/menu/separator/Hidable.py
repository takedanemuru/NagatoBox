
from libnagato.menu.Separator import NagatoSeparator
from libnagato.menu.Action import NagatoActionCore


class NagatoHidable(NagatoActionCore):

    def _on_activate(self, widget):
        pass

    def _get_visible(self):
        # Virtual
        return True

    def _on_map(self, widget):
        self._separator.set_property("visible", self._get_visible())
        self.hide()

    def _initialize_variables(self):
        self._title = "DO NOT LOOK AT ME."
        self._query = "YUKI.N > hit test result"
        self._message = ""
        self._separator = NagatoSeparator(self._parent)

