
from gi.repository import Gtk
from libnagatowebbrowser.menu.action.ActionCore import NagatoActionCore


class NagatoCloseTab(NagatoActionCore):

    def _initialize_variables(self):
        self._title = "Close Current Tab"
        self._query = "YUKI.N > has multi tabs"
        self._message = "YUKI.N > close current tab"
