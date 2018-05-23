
from gi.repository import Gdk
from libnagatoimageviewer.cairo.PixbufHandler import NagatoPixbufHandler
from libnagatoimageviewer.Prime import NagatoPrime


class NagatoContextHandler(NagatoPrime):

    def _on_draw(self, drawing_area, cairo_context):
        Gdk.cairo_set_source_pixbuf(
            cairo_context,
            *self._prime_object.source_pixbuf_with_offset
            )
        cairo_context.paint()
        self._raise("YUKI.N > paint finished", self._prime_object.size)

    def __init__(self, parent):
        self._parent = parent
        self._prime_object = NagatoPixbufHandler(self)
        self._parent.connect("draw", self._on_draw)
