
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.paint.HistoryLines import NagatoHistoryLines


class NagatoDrawingArea(Gtk.DrawingArea, NagatoObject):

    def _on_draw(self, drawing_area, cairo_context):
        self._history_lines.paint(cairo_context)

    def _inform_drawing_area_size(self):
        return self.get_allocated_width(), self.get_allocated_height()

    def _inform_histories(self):
        return self._histories

    def queue(self, histories):
        self._histories = histories
        self.queue_draw()

    def __init__(self, parent):
        self._parent = parent
        self._histories = None
        self._history_lines = NagatoHistoryLines(self)
        Gtk.DrawingArea.__init__(self)
        self.set_vexpand(True)
        self.set_hexpand(True)
        self.connect("draw", self._on_draw)
