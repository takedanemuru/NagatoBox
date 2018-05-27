
from libnagato.Object import NagatoObject


class NagatoEnterLock(NagatoObject):

    def _on_enter(self, *args):
        self._raise("YUKI.N > set lock", True)

    def _on_leave(self, *args):
        self._raise("YUKI.N > set lock", False)

    def _set_signals(self):
        self._parent.connect("enter-notify-event", self._on_enter)
        self._parent.connect("leave-notify-event", self._on_leave)

    def __init__(self, parent):
        self._parent = parent
        self._set_signals()
