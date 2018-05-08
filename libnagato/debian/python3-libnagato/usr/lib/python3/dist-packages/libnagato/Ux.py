
from gi.repository import Gdk

BASE_UNIT = int(Gdk.Screen.get_default().get_resolution() / 12)
NAMES = {
    "default-window-height": 60,
    "default-window-width": 90,
    "grid-spacing": 2,
    "padding": 1
    }


def Unit(arg):
    if isinstance(arg, int):
        return BASE_UNIT * arg
    elif arg in NAMES:
        return BASE_UNIT * NAMES[arg]
    else:
        return 0
