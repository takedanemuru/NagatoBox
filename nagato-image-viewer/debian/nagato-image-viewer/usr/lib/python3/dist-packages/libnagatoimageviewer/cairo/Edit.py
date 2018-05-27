
from libnagato.Object import NagatoObject
from libnagatoimageviewer.cairo.Rotation import NagatoRotation
from libnagatoimageviewer.cairo.Zoom import NagatoZoom


class NagatoEdit(NagatoObject):

    def get_edited(self, pixbuf):
        yuki_pixbuf = self._rotation.get_rotated(pixbuf)
        return self._zoom.get_zoomed(yuki_pixbuf)

    def __call__(self, message):
        if message.startswith("object"):
            self._rotation(message)
        if message.startswith("zoom"):
            self._zoom(message)

    def __init__(self, parent):
        self._parent = parent
        self._rotation = NagatoRotation(self)
        self._zoom = NagatoZoom(self)
