
from pathlib import Path
from libnagato.Object import NagatoObject
from libnagato.dialog.chooser.Save import NagatoSave


class NagatoPathEvents(NagatoObject):

    def _ensure(self):
        if self._path is None:
            self._path = NagatoSave.call()

    def new(self):
        self._path = None
        self._raise("YUKI.N > path event", ("clear text", self._path))

    def load(self, path):
        self._path = path
        self._raise("YUKI.N > path event", ("set text", self._path))

    def save(self):
        self._ensure()
        if self._path is not None:
            self._raise("YUKI.N > path event", ("save text", self._path))
        return (self._path is not None)

    def save_as(self, path):
        self._path = path
        self._raise("YUKI.N > path event", ("save text", self._path))

    def _set_first_path(self):
        yuki_path = self._enquiry("YUKI.N > args", "path")
        if yuki_path is None:
            return
        if Path(yuki_path).exists():
            self.load(yuki_path)

    def __init__(self, parent):
        self._parent = parent
        self._path = None
        self._set_first_path()
