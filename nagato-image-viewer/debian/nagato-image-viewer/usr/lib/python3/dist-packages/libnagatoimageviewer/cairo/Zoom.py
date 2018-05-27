
from gi.repository import GdkPixbuf
from libnagato.Object import NagatoObject
from libnagatoimageviewer.Mikuru import Rect
from libnagatoimageviewer.Mikuru import CallDispatch

INTERP_TYPE = GdkPixbuf.InterpType.BILINEAR


class NagatoZoom(NagatoObject):

    def _on_zoom_fit_best(self):
        self._fit = True

    def _on_zoom_in(self):
        self._fit = False
        self._zoom = self._zoom*1.1

    def _on_zoom_out(self):
        self._fit = False
        self._zoom = self._zoom*0.9

    def _on_zoom_original(self):
        self._fit = False
        self._zoom = 1

    def _recalc_fit_rate(self, inner_size):
        if self._fit:
            yuki_outer_size = self._enquiry("YUKI.N > drawing area size")
            self._zoom = Rect.get_zoom_rate(yuki_outer_size, inner_size)

    def get_zoomed(self, pixbuf):
        yuki_w, yuki_h = pixbuf.get_width(), pixbuf.get_height()
        self._recalc_fit_rate((yuki_w, yuki_h))
        yuki_zoomed_w, yuki_zoomed_h = yuki_w*self._zoom, yuki_h*self._zoom
        return pixbuf.scale_simple(yuki_zoomed_w, yuki_zoomed_h, INTERP_TYPE)

    def __call__(self, message):
        yuki_method = getattr(self, self._call_dispatch[message])
        yuki_method()

    def __init__(self, parent):
        self._parent = parent
        self._call_dispatch = CallDispatch.ZOOM
        self._fit = True
        self._zoom = 1
