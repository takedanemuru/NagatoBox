
from libnagato.Object import NagatoObject
from libnagato.util import PangoFont
from gi.repository import Gdk


class NagatoAttributes(NagatoObject):

    def _set_font(self):
        yuki_font = self._enquiry("YUKI.N > config", ("vte", "font"))
        self._parent.set_font(PangoFont.get(yuki_font))

    def _get_color(self, key):
        yuki_color_value = self._enquiry("YUKI.N > config", ("vte", key))
        yuki_gdk_rgba = Gdk.RGBA()
        yuki_gdk_rgba.parse(yuki_color_value)
        return yuki_gdk_rgba

    def _refresh(self):
        self._set_font()
        self._parent.set_color_foreground(self._get_color("foreground_color"))
        self._parent.set_color_background(self._get_color("background_color"))

    def refresh(self):
        self._refresh()

    def __init__(self, parent):
        self._parent = parent
        self._parent.set_allow_bold(False)
        self._parent.set_scrollback_lines(-1)
        self._refresh()
