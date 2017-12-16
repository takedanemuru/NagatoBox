
from gi.repository import Gtk
from libnagatowebbrowser.menu.item.sensitive.Core import NagatoCore


class NagatoStopLoading(NagatoCore):

    def _initialize_variables(self):
        self._title = "Stop Loading"
        self._query = "YUKI.N > can stop loading"
        self._message = "YUKI.N > stop loading"
