
GRID_SPACING = 16


class NagatoFlexGridAttributes(object):

    def __init__(self, grid):
        self._grid = grid
        self._grid.set_column_homogeneous(True)
        self._grid.set_row_homogeneous(True)
        self._grid.set_border_width(GRID_SPACING)
        self._grid.set_row_spacing(GRID_SPACING)
        self._grid.set_column_spacing(GRID_SPACING)
