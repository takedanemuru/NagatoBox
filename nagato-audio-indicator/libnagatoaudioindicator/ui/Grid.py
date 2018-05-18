
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatoaudioindicator.eventbox.ForLabel import NagatoEventBox

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
        self.attach(NagatoEventBox(self), 0, 0, 1, 1)
