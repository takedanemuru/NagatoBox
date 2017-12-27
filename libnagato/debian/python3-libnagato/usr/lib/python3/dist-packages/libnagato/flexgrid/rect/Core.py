
from gi.repository import Gtk
from libnagato.datatype.Rect import NagatoRect


class NagatoCore(object):

    def _get_offset_rect(self, left, top, width, height):
        yuki_rect = NagatoRect(
            self._rect._left + left,
            self._rect._top + top,
            self._rect._width + width,
            self._rect._height + height,
            )
        return yuki_rect

    def __call__(self, gtk_position_type):
        if gtk_position_type == Gtk.PositionType.RIGHT:
            return self._get_right()
        if gtk_position_type == Gtk.PositionType.BOTTOM:
            return self._get_bottom()
        if gtk_position_type == Gtk.PositionType.TOP:
            return self._get_top()
        if gtk_position_type == Gtk.PositionType.LEFT:
            return self._get_left()

    def __init__(self, rect):
        self._rect = rect
