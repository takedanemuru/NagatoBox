
from gi.repository import Gtk
from libnagatowebbrowser.menu.item.sensitive.Core import NagatoCore


class NagatoGoBack(NagatoCore):

    def _initialize_variables(self):
        self._title = "Go Back"
        self._query = "YUKI.N > can go back"
        self._message = "YUKI.N > go back"
