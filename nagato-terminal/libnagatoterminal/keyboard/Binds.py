
from libnagato.Object import NagatoObject
from libnagatoterminal.keyboard.ModKeys import NagatoModKeys

CTRL_SHIFT_BINDS = {
    67: "YUKI.N > copy",
    86: "YUKI.N > paste",
    81: "YUKI.N > destroy",
    84: "YUKI.N > add new tab"
    }


class NagatoBinds(NagatoObject):

    def _ctrl_with_shift(self, keyval):
        if keyval in CTRL_SHIFT_BINDS:
            self._raise(CTRL_SHIFT_BINDS[keyval])
        else:
            return False
        return True

    def _on_key_press(self, widget, event, user_data=None):
        self._mod_keys.reset(event.state)
        if self._mod_keys.ctrl_with_shift:
            return self._ctrl_with_shift(event.keyval)
        return False

    def __init__(self, parent):
        self._parent = parent
        self._mod_keys = NagatoModKeys()
        self._parent.connect("key-press-event", self._on_key_press)
