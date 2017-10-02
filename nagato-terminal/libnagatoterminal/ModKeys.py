
from gi.repository import Gdk

MASK_COTROL = Gdk.ModifierType.CONTROL_MASK
MASK_SHIFT = Gdk.ModifierType.SHIFT_MASK
MASK_ALT = Gdk.ModifierType.MOD1_MASK
MASK_CTRL_SHIFT = MASK_COTROL | MASK_SHIFT


class NagatoModKeys(object):

    def reset(self, keyevent_state):
        self._state = keyevent_state

    @property
    def alt(self):
        return (MASK_ALT & self._state == MASK_ALT)

    @property
    def ctrl_with_shift(self):
        return (MASK_CTRL_SHIFT & self._state == MASK_CTRL_SHIFT)
