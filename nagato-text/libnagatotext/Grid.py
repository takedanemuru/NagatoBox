
from gi.repository import Gtk
from libnagato.Ux import Unit
from libnagatotext.source.ScrolledWindow import NagatoScrolledWindow
from libnagatotext.Prime import NagatoPrime


class NagatoGrid(Gtk.Grid, NagatoPrime):

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_border_width(Unit("grid-spacing"))
        self.set_row_spacing(Unit("grid-spacing"))
        self.set_column_spacing(Unit("grid-spacing"))

    def __init__(self, parent):
        self._parent = parent
        self._initialize_grid()
        self._parent.add(self)
        self._prime_object = NagatoScrolledWindow(self)
        self.attach(self._prime_object, 0, 1, 1, 1)
