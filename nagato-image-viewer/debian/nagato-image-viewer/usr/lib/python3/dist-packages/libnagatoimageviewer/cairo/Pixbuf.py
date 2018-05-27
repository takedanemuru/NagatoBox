
from gi.repository import GdkPixbuf
from libnagatoimageviewer.Mikuru import Rect
from libnagatoimageviewer.Prime import NagatoPrime
from libnagatoimageviewer.cairo.Edit import NagatoEdit


class NagatoPixbuf(NagatoPrime):

    def _set_pixbufs(self):
        yuki_path = self._enquiry("YUKI.N > file path")
        self._original = GdkPixbuf.Pixbuf.new_from_file(yuki_path)
        self._source = self._edit.get_edited(self._original.copy())

    def _dispatch(self, header, message, user_data):
        if message == "new-file":
            self._set_pixbufs()
        else:
            self._edit(message)
            self._source = self._edit.get_edited(self._original.copy())
        self._raise("YUKI.N > queue draw")

    def __init__(self, parent):
        self._parent = parent
        self._edit = NagatoEdit(self)
        self._set_pixbufs()

    @property
    def source_pixbuf_with_offset(self):
        yuki_outer_size = self._enquiry("YUKI.N > drawing area size")
        yuki_x, yuki_y = Rect.get_offset(yuki_outer_size, self.size)
        return self._source, yuki_x, yuki_y

    @property
    def size(self):
        return self._source.get_width(), self._source.get_height()
