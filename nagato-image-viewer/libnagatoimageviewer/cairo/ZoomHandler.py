
from gi.repository import GdkPixbuf
from libnagato.Object import NagatoObject
from libnagatoimageviewer.Mikuru import Rect


class NagatoZoomHandler(NagatoObject):

    def recalc_fit(self):
        yuki_outer_size = self._enquiry("YUKI.N > drawing area size")
        yuki_inner_size = self._enquiry("YUKI.N > pixbuf size")
        self._zoom = Rect.get_zoom_rate(yuki_outer_size, yuki_inner_size)

    def get_zoomed(self, pixbuf):
        return pixbuf.scale_simple(
            pixbuf.get_width()*self._zoom,
            pixbuf.get_height()*self._zoom,
            GdkPixbuf.InterpType.BILINEAR
            ).copy()

    def __init__(self, parent):
        self._parent = parent
        self._fit = True
        self._zoom = 1
