
from gi.repository import Gtk
from libnagato.flexgrid.rect.Core import NagatoCore


class NagatoAdjust(NagatoCore):

    def _insert_column(self, column):
        if self._rect._left >= column:
            self._rect._left += 1
        elif (self._rect.right >= column > self._rect.left):
            self._rect._width += 1

    def _insert_row(self, row):
        if self._rect.top >= row:
            self._rect._top += 1
        elif (self._rect.bottom >= row > self._rect.top):
            self._rect._height += 1

    def adjust(self, gtk_position_type, new_rect):
        if gtk_position_type == Gtk.PositionType.RIGHT:
            self._insert_column(new_rect.right)
        if gtk_position_type == Gtk.PositionType.BOTTOM:
            self._insert_row(new_rect.bottom)
        if gtk_position_type == Gtk.PositionType.TOP:
            self._insert_row(new_rect.top+1)
        if gtk_position_type == Gtk.PositionType.LEFT:
            self._insert_column(new_rect.left+1)
