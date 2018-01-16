
from gi.repository import Gtk
from libnagato.menu.Action import NagatoActionCore


class NagatoStopLoading(NagatoActionCore):

    def _initialize_variables(self):
        self._title = "Stop Loading"
        self._query = "YUKI.N > can stop loading"
        self._message = "YUKI.N > stop loading"
