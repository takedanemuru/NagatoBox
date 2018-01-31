
from gi.repository import Gtk
from gi.repository import Gdk
from libnagato.Object import NagatoObject

GRID_SPACING = 16


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_border_width(GRID_SPACING)
        self.set_row_spacing(GRID_SPACING)
        self.set_column_spacing(GRID_SPACING)

    def __init__(self, parent):
        self._parent = parent
        self._initialize_grid()
        self._parent.add(self)
        self._color_selection = Gtk.ColorSelection()
        self._color_selection.set_border_width(GRID_SPACING)
        self._color_selection.set_current_rgba(
            Gdk.RGBA(1, 1, 1, 1)
            )
        self.attach(self._color_selection, 0, 0, 1, 1)
