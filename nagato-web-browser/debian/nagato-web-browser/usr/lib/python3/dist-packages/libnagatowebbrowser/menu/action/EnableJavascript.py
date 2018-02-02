
from libnagato.menu.Action import NagatoActionCore


class NagatoEnableJavascript(NagatoActionCore):

    def _on_activate(self, widget):
        self._raise(self._message)

    def _on_map(self, widget):
        if self._enquiry(self._query):
            self.set_label("Disable Javascript")
        else:
            self.set_label("Enable Javascript")
        self.show()

    def _initialize_variables(self):
        self._title = "DO NOT LOOK AT ME !!"
        self._query = "YUKI.N > javascript enabled"
        self._message = "YUKI.N > toggle javascript"
