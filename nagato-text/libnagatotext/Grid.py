
from gi.repository import Gtk
from libnagatotext.ScrolledWindow import NagatoScrolledWindow
from libnagatotext.Prime import NagatoPrime

GRID_SPACING = 16


class NagatoGrid(Gtk.Grid, NagatoPrime):

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_border_width(GRID_SPACING)
        self.set_row_spacing(GRID_SPACING)
        self.set_column_spacing(GRID_SPACING)

    def __init__(self, parent):
        self._parent = parent
        self._initialize_grid()
        self._parent.add(self)
        self._prime_object = NagatoScrolledWindow(self)
        self.attach(self._prime_object, 0, 1, 1, 1)
