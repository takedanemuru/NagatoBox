
from gi.repository import Gtk
from itertools import product
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.GridAutomata import NagatoGridAutomata


class NagatoGridAutomataVteExpand(NagatoGridAutomata):

    def _get_product(self, rect):
        yuki_columns = range(rect.left, rect.right+1)
        yuki_rows = range(rect.top, rect.bottom+1)
        return product(yuki_columns, yuki_rows)

    def _exists(self, vte, rect):
        for yuki_column, yuki_row in self._get_product(rect):
            yuki_vte = self._grid.get_child_at(yuki_column, yuki_row)
            if yuki_vte is not None and yuki_vte != vte:
                return True
        return False            

    def _to_left(self, vte, rect):
        self._adjust_positions(vte, rect, Gtk.PositionType.LEFT)
        return NagatoRect(rect.left+1, rect.top, rect.width, rect.height)

    def _to_top(self, vte, rect):
        self._adjust_positions(vte, rect, Gtk.PositionType.TOP)
        return NagatoRect(rect.left, rect.top+1, rect.width, rect.height)

    def _to_else(self, vte, rect, gtk_position_type):
        self._adjust_positions(vte, rect, gtk_position_type)
        return rect
