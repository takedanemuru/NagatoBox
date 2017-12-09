
from gi.repository import Gtk
from libnagatoterminal.RectAutomata import NagatoRectAutomata

HORIZONTALS = [Gtk.PositionType.RIGHT, Gtk.PositionType.LEFT]

class NagatoRectAutomataShrink(NagatoRectAutomata):

    def _get_right(self):
        return self._get_offset_rect(1, 0, -1, 0)

    def _get_bottom(self):
        return self._get_offset_rect(0, 1, 0, -1)

    def _get_top(self):
        return self._get_offset_rect(0, 0, 0, -1)

    def _get_left(self):
        return self._get_offset_rect(0, 0, -1, 0)

    def can_shrink_to(self, gtk_position_type):
        if gtk_position_type in HORIZONTALS:
            return (self._rect._width >= 2)
        else:
            return (self._rect._height >= 2)
