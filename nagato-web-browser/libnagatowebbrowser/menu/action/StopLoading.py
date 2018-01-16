
from gi.repository import Gtk
from libnagato.menu.Action import NagatoActionCore


class NagatoStopLoading(NagatoActionCore):

    def _on_map(self, widget):
        if not self._enquiry(self._query):
            self.hide()
        else:
            self.show()

    def _initialize_variables(self):
        self._title = "Stop Loading"
        self._query = "YUKI.N > can stop loading"
        self._message = "YUKI.N > stop loading"
