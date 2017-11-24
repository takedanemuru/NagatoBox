
from gi.repository import Gtk
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.GridAutomata import NagatoGridAutomata


class NagatoGridAutomataVteExpand(NagatoGridAutomata):

    def _can_expand_to(self, vte, rect):
        for yuki_column in range(rect.left, rect.right+1):
            for yuki_row in range(rect.top, rect.bottom+1):
                yuki_vte = self._grid.get_child_at(yuki_column, yuki_row)
                if yuki_vte is not None and yuki_vte != vte:
                    return False
        return True

    def _to_left(self, vte, rect):
        if self._can_expand_to(vte, rect):
            return rect
        else:
            self._adjust_positions(vte, rect, Gtk.PositionType.LEFT)
            return NagatoRect(rect.left+1, rect.top, rect.width, rect.height)

    def _to_top(self, vte, rect):
        if self._can_expand_to(vte, rect):
            return rect
        else:
            self._adjust_positions(vte, rect, Gtk.PositionType.TOP)
            return NagatoRect(rect.left, rect.top+1, rect.width, rect.height)

    def _to_else(self, vte, rect, gtk_position_type):
        if not self._can_expand_to(vte, rect):
            self._adjust_positions(vte, rect, gtk_position_type)
        return rect
