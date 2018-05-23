
from libnagato.Object import NagatoObject


class NagatoIndex(NagatoObject):

    def go_next(self):
        self._index += 1
        if self._index >= self._enquiry("YUKI.N > max index"):
            self._index = 0

    def go_previous(self):
        self._index -= 1
        if 0 > self._index:
            self._index = self._enquiry("YUKI.N > max index")

    def reset(self, index):
        self._index = index

    def __init__(self, parent):
        self._parent = parent
        self._index = 0

    @property
    def index(self):
        return self._index
