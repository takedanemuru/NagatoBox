
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.Ux import Unit
from libnagatoimageviewer.files.Files import NagatoFiles
from libnagatoimageviewer.ui.ScrolledWindow import NagatoScrolledWindow
from libnagatoimageviewer.ui.ActionBar import NagatoActionBar


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _yuki_n_view(self, user_data):
        self._scrolled_window.prime_call(user_data)

    def _yuki_n_file(self, user_data):
        self._file_handler(user_data)
        self._scrolled_window.prime_call("new-file")

    def _inform_file_path(self):
        return self._file_handler.path

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_row_spacing(Unit("grid-spacing"))
        self.set_column_spacing(Unit("grid-spacing"))

    def __init__(self, parent):
        self._parent = parent
        self._initialize_grid()
        self._parent.add(self)
        self._file_handler = NagatoFiles(self)
        self._scrolled_window = NagatoScrolledWindow(self)
        self.attach(self._scrolled_window, 0, 0, 1, 1)
        self.attach(NagatoActionBar(self), 0, 1, 1, 1)
