
from libnagato.Object import NagatoObject
from libnagatoimageviewer.Mikuru import CallDispatch


class NagatoRotation(NagatoObject):

    def _on_rotate_left(self):
        self._angle += 90

    def _on_rotate_right(self):
        self._angle -= 90

    def _on_flip_vertical(self):
        self._flip_vertical = not self._flip_vertical

    def _on_flip_horizontal(self):
        self._flip_horizontal = not self._flip_horizontal

    def get_rotated(self, pixbuf):
        yuki_pixbuf = pixbuf.rotate_simple(self._angle % 360)
        if self._flip_horizontal:
            yuki_pixbuf = yuki_pixbuf.flip(True)
        if self._flip_vertical:
            yuki_pixbuf = yuki_pixbuf.flip(False)
        return yuki_pixbuf.copy()

    def __call__(self, message):
        yuki_method = getattr(self, self._call_dispatch[message])
        yuki_method()

    def __init__(self, parent):
        self._parent = parent
        self._call_dispatch = CallDispatch.ROTATION
        self._angle = 0
        self._flip_horizontal = False
        self._flip_vertical = False
