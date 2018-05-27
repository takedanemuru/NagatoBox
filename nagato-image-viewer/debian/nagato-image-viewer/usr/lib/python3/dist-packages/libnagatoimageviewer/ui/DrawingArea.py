
from gi.repository import Gtk
from libnagatoimageviewer.cairo.ContextHandler import NagatoContextHandler
from libnagatoimageviewer.Prime import NagatoPrime


class NagatoDrawingArea(Gtk.DrawingArea, NagatoPrime):

    def _yuki_n_queue_draw(self):
        self.queue_draw()

    def _yuki_n_paint_finished(self, image_size):
        self.set_size_request(*image_size)

    def _on_map(self, widget):
        # drawing area should return allocated size (0, 0)
        # when it's not mapped.
        self._prime_object = NagatoContextHandler(self)

    def __init__(self, parent):
        self._parent = parent
        Gtk.DrawingArea.__init__(self)
        self.set_hexpand(True)
        self.set_vexpand(True)
        self.connect("map", self._on_map)
        self._parent.add(self)
