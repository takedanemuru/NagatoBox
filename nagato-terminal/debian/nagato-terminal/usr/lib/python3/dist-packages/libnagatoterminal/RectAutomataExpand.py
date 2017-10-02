
from gi.repository import Gtk
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.RectAutomata import NagatoRectAutomata


class NagatoRectAutomataExpand(NagatoRectAutomata):

    def get_new_vte_rect(self, gtk_position_type):
        if gtk_position_type == Gtk.PositionType.RIGHT:
            return NagatoRect(self._rect.right+1, self._rect._top)
        elif gtk_position_type == Gtk.PositionType.BOTTOM:
            return NagatoRect(self._rect._left, self._rect.bottom+1)
        elif gtk_position_type == Gtk.PositionType.TOP:
            return NagatoRect(self._rect._left, self._rect._top-1)
        elif gtk_position_type == Gtk.PositionType.LEFT:
            return NagatoRect(self._rect._left-1, self._rect._top)

    def get_expanded_rect(self, gtk_position_type):
        if gtk_position_type == Gtk.PositionType.RIGHT:
            return self._get_offset_rect(0, 0, 1, 0)
        elif gtk_position_type == Gtk.PositionType.BOTTOM:
            return self._get_offset_rect(0, 0, 0, 1)
        elif gtk_position_type == Gtk.PositionType.TOP:
            return self._get_offset_rect(0, -1, 0, 1)
        elif gtk_position_type == Gtk.PositionType.LEFT:
            return self._get_offset_rect(-1, 0, 1, 0)
