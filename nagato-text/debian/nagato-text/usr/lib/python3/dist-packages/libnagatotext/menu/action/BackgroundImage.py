
from libnagato.menu.Action import NagatoActionCore
from libnagato.dialog.chooser.Load import NagatoLoad

class NagatoBackgroundImage(NagatoActionCore):

    def _on_activate(self, widget):
        yuki_path = NagatoLoad.call(mime_type="image/*")
        if yuki_path is not None:
            yuki_data = "css", "background_image", yuki_path
            self._raise("YUKI.N > config", yuki_data)

    def _on_map(self, widget):
        pass

    def _initialize_variables(self):
        self._title = "Background Image"
        self._query = ""
        self._message = ""
