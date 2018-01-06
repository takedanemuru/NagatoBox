
from gi.repository import Gdk
from libnagato.Object import NagatoObject
from libnagatowebbrowser.util.TimeDeltaLock import NagatoTimeDeltaLock

MASK_ALT = Gdk.ModifierType.MOD1_MASK


class NagatoBinds(NagatoObject):

    def _on_key_press(self, widget, event, user_data=None):
        yuki_keyval_name = Gdk.keyval_name(event.keyval)
        if yuki_keyval_name == "F11":
            self._emmit_toggle_fullscreen()
        if not (MASK_ALT & event.state == MASK_ALT):
            return
        if yuki_keyval_name == "Left":
            self._raise("YUKI.N > go back")
        if yuki_keyval_name == "Right":
            self._raise("YUKI.N > go forward")

    def _emmit_toggle_fullscreen(self):
        # I don't know why, but
        # Webkit2 fires F11 event twice.
        if self._time_delta_lock.check_diff(0.5):
            self._raise("YUKI.N > toggle fullscreen")

    def __init__(self, parent):
        self._parent = parent
        self._parent.connect("key-press-event", self._on_key_press)
        self._time_delta_lock = NagatoTimeDeltaLock()
