
from gi.repository import Gtk
from libnagato.datatype.Rect import NagatoRect
from libnagato.flexgrid.adjust.Core import NagatoAdjustCore


class NagatoNew(NagatoAdjustCore):

    def _exists(self, notebook, rect):
        if self._grid.get_child_at(rect.left, rect.top) is None:
            return False
        return True

    def _to_left(self, notebook, rect):
        self._adjust_positions(notebook, rect, Gtk.PositionType.LEFT)
        return NagatoRect(rect.left+1, rect.top)

    def _to_top(self, notebook, rect):
        self._adjust_positions(notebook, rect, Gtk.PositionType.TOP)
        return NagatoRect(rect.left, rect.top+1)

    def _to_else(self, notebook, rect, gtk_position_type):
        self._adjust_positions(notebook, rect, gtk_position_type)
        return rect
