
from gi.repository import Gtk
from libnagatoterminal.RectAutomata import NagatoRectAutomata


class NagatoRectAutomataAdjust(NagatoRectAutomata):

    def _at_within(self, insert_position, start, end):
        if end >= insert_position and insert_position > start:
            return True
        return False

    def _insert_column(self, column):
        if self._rect._left >= column:
            self._rect._left += 1
        elif self._at_within(column, self._rect.left, self._rect.right):
            self._rect._width += 1

    def _insert_row(self, row):
        if self._rect.top >= row:
            self._rect._top += 1
        elif self._at_within(row, self._rect.top, self._rect.bottom):
            self._rect._height += 1

    def adjust(self, gtk_position_type, rect):
        if gtk_position_type == Gtk.PositionType.RIGHT:
            self._insert_column(rect.right)
        elif gtk_position_type == Gtk.PositionType.BOTTOM:
            self._insert_row(rect.bottom)
        elif gtk_position_type == Gtk.PositionType.TOP:
            self._insert_row(rect.top+1)
        elif gtk_position_type == Gtk.PositionType.LEFT:
            self._insert_column(rect.left+1)
