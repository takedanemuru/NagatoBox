
from libnagatowebbrowser.menu.action.ActionCore import NagatoActionCore


class NagatoFullScreen(NagatoActionCore):

    def _on_activate(self, widget):
        self._raise(self._message)

    def _on_map(self, widget):
        if self._enquiry(self._query):
            self.set_label("Exit Fullscreen")
        else:
            self.set_label("Fullscreen")
        self.show()

    def _initialize_variables(self):
        self._title = "DO NOT LOOK AT ME !!"
        self._query = "YUKI.N > is fullscreen"
        self._message = "YUKI.N > toggle fullscreen"
