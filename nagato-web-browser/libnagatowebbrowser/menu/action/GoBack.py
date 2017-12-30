
from gi.repository import Gtk
from libnagatowebbrowser.menu.action.ActionCore import NagatoActionCore


class NagatoGoBack(NagatoActionCore):

    def _initialize_variables(self):
        self._title = "Go Back"
        self._query = "YUKI.N > can go back"
        self._message = "YUKI.N > go back"
