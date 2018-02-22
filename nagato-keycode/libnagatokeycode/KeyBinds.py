
from gi.repository import Gdk
from libnagato.Object import NagatoObject


class NagatoKeyBinds(NagatoObject):

    def _on_key_press(self, widget, event, user_data=None):
        self._raise("YUKI.N > keyval", event.keyval)

    def __init__(self, parent):
        self._parent = parent
        self._parent.add_events(Gdk.EventMask.KEY_PRESS_MASK)
        self._parent.set_can_focus(True)
        self._parent.connect("key-press-event", self._on_key_press)
