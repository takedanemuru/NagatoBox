
from gi.repository import Gtk
from libnagato.Object import NagatoObject

STEP = 5


class NagatoDrawingArea(Gtk.DrawingArea, NagatoObject):

    def _initialize(self, first_history):
        yuki_h = self.get_allocated_height()
        yuki_x = self.get_allocated_width()
        yuki_y = yuki_h-(first_history*yuki_h)
        return yuki_x, yuki_y, yuki_h

    def _draw_line(self, cairo_context, history, red=0, green=0, blue=0):
        if len(history) == 0:
            return
        cairo_context.set_source_rgb(red, green, blue)
        yuki_x, yuki_y, yuki_h = self._initialize(history.pop())
        cairo_context.move_to(yuki_x, yuki_y)
        while len(history) > 1 and yuki_y > 0:
            yuki_x -= STEP
            cairo_context.line_to(yuki_x, yuki_y)
            yuki_y = max(1, yuki_h-(history.pop()*yuki_h))
            cairo_context.line_to(yuki_x, yuki_y)
        cairo_context.stroke()

    def _on_draw(self, drawing_area, cairo_context):
        if self._histories is None:
            return
        cairo_context.set_line_width(1)
        self._draw_line(cairo_context, self._histories["cpu"], red=1)
        self._draw_line(cairo_context, self._histories["memory"], blue=1)
        self._draw_line(cairo_context, self._histories["swap"], green=1)

    def queue(self, histories):
        self._histories = histories
        self.queue_draw()

    def __init__(self, parent):
        self._parent = parent
        self._histories = None
        Gtk.DrawingArea.__init__(self)
        self.set_vexpand(True)
        self.set_hexpand(True)
        self.connect("draw", self._on_draw)
