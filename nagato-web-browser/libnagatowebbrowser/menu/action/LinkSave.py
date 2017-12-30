
from libnagatowebbrowser.menu.action.LinkCore import NagatoLinkCore


class NagatoLinkSave(NagatoLinkCore):

    def _on_activate(self, widget):
        pass

    def _initialize_variables(self):
        self._title = "Save Link"
        self._query = "YUKI.N > hit test result"
        self._message = ""
