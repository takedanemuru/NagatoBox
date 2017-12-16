
from gi.repository import Gtk
from libnagatowebbrowser.menu.item.sensitive.Core import NagatoCore


class NagatoGoForward(NagatoCore):

    def _initialize_variables(self):
        self._title = "Go Forward"
        self._query = "YUKI.N > can go forward"
        self._message = "YUKI.N > go forward"
