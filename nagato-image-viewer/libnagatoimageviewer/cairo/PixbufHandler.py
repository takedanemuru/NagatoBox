
from gi.repository import GdkPixbuf
from libnagatoimageviewer.cairo.ZoomHandler import NagatoZoomHandler
from libnagatoimageviewer.Mikuru import Rect
from libnagatoimageviewer.Prime import NagatoPrime


class NagatoPixbufHandler(NagatoPrime):

    def _inform_pixbuf_size(self):
        return self._original.get_width(), self._original.get_height()

    def _set_original_pixbuf(self):
        yuki_path = self._enquiry("YUKI.N > file path")
        self._original = GdkPixbuf.Pixbuf.new_from_file(yuki_path)
        self._zoom.recalc_fit()
        self._source = self._zoom.get_zoomed(self._original.copy())

    def _dispatch(self, header, message, user_data):
        if message == "refresh":
            self._set_original_pixbuf()
        self._raise("YUKI.N > queue draw")

    def __init__(self, parent):
        self._parent = parent
        self._zoom = NagatoZoomHandler(self)
        self._set_original_pixbuf()

    @property
    def source_pixbuf_with_offset(self):
        yuki_outer_size = self._enquiry("YUKI.N > drawing area size")
        yuki_x, yuki_y = Rect.get_offset(yuki_outer_size, self.size)
        return self._source, yuki_x, yuki_y

    @property
    def size(self):
        return self._source.get_width(), self._source.get_height()
