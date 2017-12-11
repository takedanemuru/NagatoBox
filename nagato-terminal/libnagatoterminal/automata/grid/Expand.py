
from gi.repository import Gtk
from itertools import product
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.automata.grid.Core import NagatoCore


class NagatoExpand(NagatoCore):

    def _get_product(self, rect):
        yuki_columns = range(rect.left, rect.right+1)
        yuki_rows = range(rect.top, rect.bottom+1)
        return product(yuki_columns, yuki_rows)

    def _exists(self, notebook, rect):
        for yuki_column, yuki_row in self._get_product(rect):
            yuki_notebook = self._grid.get_child_at(yuki_column, yuki_row)
            if yuki_notebook is not None and yuki_notebook != notebook:
                return True
        return False

    def _to_left(self, notebook, rect):
        self._adjust_positions(notebook, rect, Gtk.PositionType.LEFT)
        return NagatoRect(rect.left+1, rect.top, rect.width, rect.height)

    def _to_top(self, notebook, rect):
        self._adjust_positions(notebook, rect, Gtk.PositionType.TOP)
        return NagatoRect(rect.left, rect.top+1, rect.width, rect.height)

    def _to_else(self, notebook, rect, gtk_position_type):
        self._adjust_positions(notebook, rect, gtk_position_type)
        return rect
