
from gi.repository import Gdk


def get_transparent():
    return Gdk.RGBA(0, 0, 0, 0)


def get_color(red, green, blue, alpha):
    return Gdk.RGBA(red, green, blue, alpha)


def get(color):
    yuki_color = Gdk.RGBA()
    yuki_color.parse(color)
    return yuki_color
