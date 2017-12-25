
from gi.repository import Gtk


class NagatoAdjustCore(object):

    def _adjust_positions(self, vte, rect, gtk_position_type):
        self._grid.insert_next_to(vte, gtk_position_type)
        for yuki_vte in self._grid.get_children():
            yuki_vte.adjust_position(gtk_position_type, rect)

    def _get_rect(self, vte, gtk_position_type, rect):
        if gtk_position_type == Gtk.PositionType.LEFT:
            return self._to_left(vte, rect)
        elif gtk_position_type == Gtk.PositionType.TOP:
            return self._to_top(vte, rect)
        else:
            return self._to_else(vte, rect, gtk_position_type)

    def __call__(self, grid_data):
        if not self._exists(grid_data.signal_from, grid_data.destination_rect):
            return grid_data.destination_rect
        return self._get_rect(
            grid_data.signal_from,
            grid_data.direction,
            grid_data.destination_rect
            )

    def __init__(self, grid):
        self._grid = grid
