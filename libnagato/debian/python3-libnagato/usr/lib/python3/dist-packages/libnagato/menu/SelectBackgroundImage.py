
from libnagato.menu.Action import NagatoActionCore
from libnagato.dialog.chooser.Load import NagatoLoad


class NagatoSelectBackgroundImage(NagatoActionCore):

    def _on_activate(self, widget):
        yuki_path = NagatoLoad.call(mime_type="image/*")
        if yuki_path is not None:
            self._raise(self._message, self._query+(yuki_path,))

    def _on_map(self, widget):
        pass

    def _initialize_variables(self):
        self._title = "Select Background Image"
        self._query = "css", "background_image"
        self._message = "YUKI.N > config"
