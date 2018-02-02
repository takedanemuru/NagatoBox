
from gi.repository import Gtk
from libnagato.menu.Action import NagatoActionCore


class NagatoGoBack(NagatoActionCore):

    def _on_map(self, widget):
        if not self._enquiry(self._query):
            self.hide()
        else:
            self.show()

    def _initialize_variables(self):
        self._title = "Go Back"
        self._query = "YUKI.N > can go back"
        self._message = "YUKI.N > go back"
