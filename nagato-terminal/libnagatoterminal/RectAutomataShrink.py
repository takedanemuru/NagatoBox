
from gi.repository import Gtk
from libnagatoterminal.RectAutomata import NagatoRectAutomata

HORIZONTALS = [Gtk.PositionType.RIGHT, Gtk.PositionType.LEFT]

class NagatoRectAutomataShrink(NagatoRectAutomata):

    def get_rect(self, gtk_position_type):
        if gtk_position_type == Gtk.PositionType.RIGHT:
            return self._get_offset_rect(1, 0, -1, 0)
        elif gtk_position_type == Gtk.PositionType.BOTTOM:
            return self._get_offset_rect(0, 1, 0, -1)
        elif gtk_position_type == Gtk.PositionType.TOP:
            return self._get_offset_rect(0, 0, 0, -1)
        elif gtk_position_type == Gtk.PositionType.LEFT:
            return self._get_offset_rect(0, 0, -1, 0)

    def can_shrink_to(self, gtk_position_type):
        if gtk_position_type in HORIZONTALS:
            return (self._rect._width >= 2)
        else:
            return (self._rect._height >= 2)
