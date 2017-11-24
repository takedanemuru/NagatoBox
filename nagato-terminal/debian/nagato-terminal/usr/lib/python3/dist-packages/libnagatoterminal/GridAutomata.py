
from gi.repository import Gtk


class NagatoGridAutomata(object):

    def _adjust_positions(self, vte, rect, gtk_position_type):
        self._grid.insert_next_to(vte, gtk_position_type)
        for yuki_vte in self._grid.get_children():
            yuki_vte.adjust_position(gtk_position_type, rect)

    def _to_left(self, vte, rect):
        pass

    def _to_top(self, vte, rect):
        pass

    def _to_else(self, vte, rect, gtk_position_type):
        pass

    def _get_rect(self, vte, gtk_position_type, rect):
        if gtk_position_type == Gtk.PositionType.LEFT:
            return self._to_left(vte, rect)
        elif gtk_position_type == Gtk.PositionType.TOP:
            return self._to_top(vte, rect)
        else:
            return self._to_else(vte, rect, gtk_position_type)

    def __call__(self, user_data):
        yuki_rect = self._get_rect(
            user_data[0],
            user_data[1],
            user_data[2]
            )
        return yuki_rect

    def __init__(self, grid):
        self._grid = grid
