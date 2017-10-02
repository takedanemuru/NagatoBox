
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.ModKeys import NagatoModKeys
from libnagatoterminal.util import Direction

CTRL_SHIFT_BINDS = {
    67: "YUKI.N > copy",
    86: "YUKI.N > paste",
    81: "YUKI.N > destroy"
    }


class NagatoKeyBinds(NagatoObject):

    def _raise_directional_message(self, message, keyval):
        yuki_gtk_position_type = Direction.get_gtk_position_type(keyval)
        self._raise(message, yuki_gtk_position_type)

    def _alt(self, keyval):
        if Direction.is_direction(keyval):
            self._raise_directional_message("YUKI.N > expand to", keyval)
        else:
            return False
        return True

    def _ctrl_with_shift(self, keyval):
        if keyval in CTRL_SHIFT_BINDS:
            self._raise(CTRL_SHIFT_BINDS[keyval])
        elif Direction.is_direction(keyval):
            self._raise_directional_message("YUKI.N > insert to", keyval)
        else:
            return False
        return True

    def _on_key_press(self, widget, event, user_data=None):
        self._mod_keys.reset(event.state)
        if self._mod_keys.alt:
            return self._alt(event.keyval)
        elif self._mod_keys.ctrl_with_shift:
            return self._ctrl_with_shift(event.keyval)
        else:
            return False

    def __init__(self, parent, vte):
        self._parent = parent
        self._mod_keys = NagatoModKeys()
        vte.connect("key-press-event", self._on_key_press)
