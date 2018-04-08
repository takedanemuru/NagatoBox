
import os
from libnagato.Object import NagatoObject
from libnagatotext.PathHandler import NagatoPathHandler


class NagatoFileHandler(NagatoObject):

    def _is_closable(self):
        if self._saved:
            return True
        return self._path_handler.is_closable()

    def _yuki_n_saved(self):
        self._saved = True

    def new(self):
        if self._is_closable():
            self._path_handler.new()

    def load(self):
        if self._is_closable():
            self._path_handler.load()

    def save(self):
        self._path_handler.save()

    def save_as(self):
        self._path_handler.save_as()

    def _on_changed(self, text_buffer):
        self._saved = False

    def _set_first_path(self):
        yuki_path = self._enquiry("YUKI.N > args", "path")
        if yuki_path is None:
            return
        if os.path.exists(yuki_path):
            self._path_handler.load_path(yuki_path)

    def __init__(self, parent, text_buffer):
        self._parent = parent
        self._saved = True
        text_buffer.connect("changed", self._on_changed)
        self._path_handler = NagatoPathHandler(self)
        self._set_first_path()
