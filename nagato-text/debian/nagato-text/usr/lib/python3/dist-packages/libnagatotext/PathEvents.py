
from libnagato.Object import NagatoObject
from libnagatotext.dialog.FileChooserSave import NagatoFileChooserSave


class NagatoPathEvents(NagatoObject):

    def _ensure(self):
        if self._path is None:
            self._path = NagatoFileChooserSave.call()

    def _load(self, path):
        self._path = path
        self._raise("YUKI.N > set text", self._path)
        self._raise("YUKI.N > saved")

    def clear(self):
        self._path = None
        self._raise("YUKI.N > clear text")
        self._raise("YUKI.N > saved")

    def load(self, path):
        self._load(path)

    def save(self):
        self._ensure()
        if self._path is None:
            return False
        self._raise("YUKI.N > save text", self._path)
        self._raise("YUKI.N > saved")
        return True

    def save_as(self, path):
        self._raise("YUKI.N > save text", path)
        self._load(path)

    def __init__(self, parent):
        self._parent = parent
        self._path = None
