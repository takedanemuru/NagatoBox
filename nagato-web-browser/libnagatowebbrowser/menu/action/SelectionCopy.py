
from libnagatowebbrowser.menu.action.SelectionCore import NagatoSelectionCore


class NagatoSelectionCopy(NagatoSelectionCore):

    def _on_activate(self, widget):
        self._raise(self._message)

    def _initialize_variables(self):
        self._title = "Copy"
        self._query = "YUKI.N > hit test result"
        self._message = "YUKI.N > copy selection"

