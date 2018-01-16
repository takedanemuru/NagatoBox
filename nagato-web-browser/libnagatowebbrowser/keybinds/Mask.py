
from gi.repository import Gdk

ALT = Gdk.ModifierType.MOD1_MASK
CTRL = Gdk.ModifierType.CONTROL_MASK
SHIFT = Gdk.ModifierType.SHIFT_MASK
ALT_SHIFT = ALT | SHIFT
CTRL_SHIFT = CTRL | SHIFT
ALT_CTRL_SHIFT = ALT | CTRL_SHIFT
