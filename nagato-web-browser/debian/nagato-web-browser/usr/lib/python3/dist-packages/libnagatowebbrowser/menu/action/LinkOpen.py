
from libnagatowebbrowser.menu.action.LinkCore import NagatoLinkCore


class NagatoLinkOpen(NagatoLinkCore):

    def _on_activate(self, widget):
        self._raise(self._message, self._last_url)

    def _initialize_variables(self):
        self._title = "Open Link In New Tab"
        self._query = "YUKI.N > hit test result"
        self._message = "YUKI.N > create"
