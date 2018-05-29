
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.util import CssProvider
from libnagatosystemmonitor.paint.labels.Header import NagatoHeader
from libnagatosystemmonitor.paint.labels.Status import NagatoStatus
from libnagatosystemmonitor.paint.Graph import NagatoGraph


class NagatoDrawingArea(Gtk.DrawingArea, NagatoObject):

    def _on_draw(self, drawing_area, cairo_context):
        self._header_labels.paint(cairo_context)
        yuki_height = self._status_labels.paint(cairo_context)
        self._graph.paint(yuki_height, cairo_context)

    def _inform_drawing_area_size(self):
        return self.get_allocated_width(), self.get_allocated_height()

    def _inform_status(self):
        return self._status

    def _initialize_drawing_area(self):
        Gtk.DrawingArea.__init__(self)
        self.set_vexpand(True)
        self.set_hexpand(True)
        self._parent.add(self)
        CssProvider.set_to_widget(self, "DrawingAreaMini")

    def queue(self, user_data):
        self._status = user_data
        self.queue_draw()

    def __init__(self, parent):
        self._parent = parent
        self._status = None
        self._initialize_drawing_area()
        self._header_labels = NagatoHeader(self)
        self._status_labels = NagatoStatus(self)
        self._graph = NagatoGraph(self)
        self.connect("draw", self._on_draw)
