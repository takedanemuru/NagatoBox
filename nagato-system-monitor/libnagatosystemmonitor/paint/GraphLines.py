
from libnagato.Object import NagatoObject

COLORS = {
    "cpu": (0.8, 0, 0),
    "memory": (0, 0, 0.8),
    "swap": (0, 0.8, 0)
    }


class NagatoGraphLines(NagatoObject):

    def _paint_first_data(self, cairo_context, first_data):
        yuki_y = self._rect.bottom-first_data*self._rect.height
        cairo_context.move_to(self._rect.right, yuki_y)
        cairo_context.line_to(self._rect.right-10, yuki_y)
        return self._rect.right-10

    def _paint_line(self, cairo_context, key):
        yuki_history = self._histories[key]
        if 0 >= len(yuki_history):
            return
        cairo_context.set_source_rgb(*COLORS[key])
        yuki_x = self._paint_first_data(cairo_context, yuki_history.pop())
        while len(yuki_history)>0 and yuki_x >= 10:
            yuki_y = self._rect.bottom-yuki_history.pop()*self._rect.height
            cairo_context.line_to(yuki_x, yuki_y)
            yuki_x -= 10
            cairo_context.line_to(max(10, yuki_x), yuki_y)
        cairo_context.stroke()

    def paint(self, cairo_context):
        self._histories = self._enquiry("YUKI.N > histories")
        if self._histories is None:
            return
        self._rect = self._enquiry("YUKI.N > rect")
        cairo_context.set_line_width(1)
        self._paint_line(cairo_context, "cpu")
        self._paint_line(cairo_context, "memory")
        self._paint_line(cairo_context, "swap")

    def __init__(self, parent):
        self._parent = parent
