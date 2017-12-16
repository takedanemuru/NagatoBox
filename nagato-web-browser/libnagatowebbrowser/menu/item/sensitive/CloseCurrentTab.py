
from gi.repository import Gtk
from libnagatowebbrowser.menu.item.sensitive.Core import NagatoCore


class NagatoCloseCurrentTab(NagatoCore):

    def _initialize_variables(self):
        self._title = "Close Current Tab"
        self._query = "YUKI.N > has multi tabs"
        self._message = "YUKI.N > close current tab"
