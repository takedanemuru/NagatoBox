
from gi.repository import Gtk
from libnagato.menu.Action import NagatoActionCore


class NagatoGoForward(NagatoActionCore):

    def _on_map(self, widget):
        if not self._enquiry(self._query):
            self.hide()
        else:
            self.show()

    def _initialize_variables(self):
        self._title = "Go Forward"
        self._query = "YUKI.N > can go forward"
        self._message = "YUKI.N > go forward"
