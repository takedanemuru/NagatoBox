
from gi.repository import Gdk
from libnagato.Object import NagatoObject
from libnagatowebbrowser.util.TimeDeltaLock import NagatoTimeDeltaLock

MASK_ALT = Gdk.ModifierType.MOD1_MASK
MASK_CTRL = Gdk.ModifierType.CONTROL_MASK

class NagatoBinds(NagatoObject):

    def _on_with_no_mods(self, keyval_name):
        if keyval_name == "F11":
            self._raise("YUKI.N > toggle fullscreen")

    def _on_with_alt(self, keyval_name):
        if keyval_name == "Left":
            self._raise("YUKI.N > go back")
        if keyval_name == "Right":
            self._raise("YUKI.N > go forward")

    def _on_with_ctrl(self, keyval_name):
        if keyval_name == "f":
            print("find something.")
        if keyval_name == "n":
            self._raise("YUKI.N > add new tab")

    def _dispatch(self, event_state, keyval_name):
        if int(event_state) == 0:
            self._on_with_no_mods(keyval_name)
        elif (MASK_ALT & event_state == MASK_ALT):
            self._on_with_alt(keyval_name)
        elif (MASK_CTRL & event_state == MASK_CTRL):
            self._on_with_ctrl(keyval_name)

    def _on_key_press(self, widget, event, user_data=None):
        if self._time_delta_lock.check_diff(0.5):
            self._dispatch(event.state, Gdk.keyval_name(event.keyval))

    def __init__(self, parent):
        self._parent = parent
        self._parent.connect("key-press-event", self._on_key_press)
        self._time_delta_lock = NagatoTimeDeltaLock()
