
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.Ux import Unit
from libAPPNAME.eventbox.ForLabel import NagatoEventBox


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_border_width(Unit("grid-spacing"))
        self.set_row_spacing(Unit("grid-spacing"))
        self.set_column_spacing(Unit("grid-spacing"))

    def __init__(self, parent):
        self._parent = parent
        self._initialize_grid()
        self._parent.add(self)
        self.attach(NagatoEventBox(self), 0, 0, 1, 1)
