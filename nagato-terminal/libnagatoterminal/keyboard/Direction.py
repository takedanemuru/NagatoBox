
from gi.repository import Gtk

DIRECTIONS = (65361, 65362, 65363, 65664)


def is_direction(keyval):
    return keyval in DIRECTIONS


def get_gtk_position_type(keyval):
    if keyval == 65361:
        return Gtk.PositionType.LEFT
    elif keyval == 65362:
        return Gtk.PositionType.TOP
    elif keyval == 65363:
        return Gtk.PositionType.RIGHT
    elif keyval == 65364:
        return Gtk.PositionType.BOTTOM
