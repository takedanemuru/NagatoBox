
from gi.repository import Gdk
from libnagato.Object import NagatoObject

MASK_COTROL = Gdk.ModifierType.CONTROL_MASK
CTRL_BINDS = {
    110: "new",
    111: "load",
    115: "save"
    }


class NagatoKeyBinds(NagatoObject):

    def _on_key_press(self, widget, event, user_data=None):
        if event.state & MASK_COTROL == MASK_COTROL:
            if event.keyval in CTRL_BINDS:
                self._raise("YUKI.N > files", CTRL_BINDS[event.keyval])

    def __init__(self, parent):
        self._parent = parent
        self._parent.connect("key-press-event", self._on_key_press)
