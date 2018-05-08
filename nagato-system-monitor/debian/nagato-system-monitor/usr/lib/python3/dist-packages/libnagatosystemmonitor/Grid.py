
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.Ux import Unit
from libnagatosystemmonitor.StatusLabel import NagatoStatusLabel
from libnagatosystemmonitor.Thread import NagatoThread
from libnagatosystemmonitor.DrawingArea import NagatoDrawingArea
from libnagatosystemmonitor.ScrolledWindow import NagatoScrolledWindow


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _yuki_n_step_graph(self, histories):
        self._drawing_area.queue(histories)

    def _yuki_n_step_label(self, user_data):
        self._label.queue(user_data)

    def _yuki_n_step_cell(self, user_data):
        self._scrolled_window.queue(user_data)

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_border_width(Unit("grid-spacing"))
        self.set_row_spacing(Unit("grid-spacing"))
        self.set_column_spacing(Unit("grid-spacing"))
        self._parent.add(self)

    def _initialize_widgets(self):
        self._drawing_area = NagatoDrawingArea(self)
        self.attach(self._drawing_area, 0, 0, 1, 1)
        self._label = NagatoStatusLabel(self)
        self.attach(self._label, 0, 2, 1, 1)
        self._scrolled_window = NagatoScrolledWindow(self)
        self.attach(self._scrolled_window, 0, 3, 1, 2)

    def __init__(self, parent):
        self._parent = parent
        self._initialize_grid()
        self._initialize_widgets()
        self._thread = NagatoThread(self)
        self._thread.start()
