
from libnagato.Object import NagatoObject
from libnagato.datatype.Rect import NagatoRect
from libnagatosystemmonitor.paint.GraphLines import NagatoGraphLines


class NagatoGraph(NagatoObject):

    def _paint_frame(self, cairo_context):
        cairo_context.set_source_rgb(0.9, 0.9, 0.9)
        cairo_context.rectangle(
            self._rect.left,
            self._rect.top,
            self._rect.width,
            self._rect.height
            )
        cairo_context.stroke()

    def _inform_rect(self):
        return self._rect

    def paint(self, label_height, cairo_context):
        yuki_width, yuki_height = self._enquiry("YUKI.N > drawing area size")
        yuki_rect_width = yuki_width-20
        yuki_rect_height = yuki_height-(30+label_height)
        self._rect = NagatoRect(10, 10, yuki_rect_width, yuki_rect_height)
        self._paint_frame(cairo_context)
        self._lines.paint(cairo_context)

    def __init__(self, parent):
        self._parent = parent
        self._lines = NagatoGraphLines(self)
