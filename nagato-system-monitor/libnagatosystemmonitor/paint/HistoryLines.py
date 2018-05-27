
from libnagato.Object import NagatoObject

STEP = 5


class NagatoHistoryLines(NagatoObject):

    def _initialize(self, first_history):
        yuki_x, yuki_h = self._enquiry("YUKI.N > drawing area size")
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

    def paint(self, cairo_context):
        yuki_histories = self._enquiry("YUKI.N > histories")
        if yuki_histories is None:
            return
        cairo_context.set_line_width(1)
        self._draw_line(cairo_context, yuki_histories["cpu"], red=1)
        self._draw_line(cairo_context, yuki_histories["memory"], blue=1)
        self._draw_line(cairo_context, yuki_histories["swap"], green=1)

    def __init__(self, parent):
        self._parent = parent
