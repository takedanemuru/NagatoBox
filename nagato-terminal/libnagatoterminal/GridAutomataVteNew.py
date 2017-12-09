
from gi.repository import Gtk
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.GridAutomata import NagatoGridAutomata


class NagatoGridAutomataVteNew(NagatoGridAutomata):

    def _exists(self, vte, rect):
        if self._grid.get_child_at(rect.left, rect.top) is None:
            return False
        return True

    def _to_left(self, vte, rect):
        self._adjust_positions(vte, rect, Gtk.PositionType.LEFT)
        return NagatoRect(rect.left+1, rect.top)

    def _to_top(self, vte, rect):
        self._adjust_positions(vte, rect, Gtk.PositionType.TOP)
        return NagatoRect(rect.left, rect.top+1)

    def _to_else(self, vte, rect, gtk_position_type):
        self._adjust_positions(vte, rect, gtk_position_type)
        return rect
