
from gi.repository import GdkPixbuf

INTERP_TYPE = GdkPixbuf.InterpType.NEAREST


class NagatoIconImage(object):

    def save_to(self, path):
        print(path)
        return self._pixbuf.savev(path, "png", [None], [])

    def get_scaled(self, maximum_size):
        if maximum_size >= max(self._width, self._height):
            return self._pixbuf
        yuki_rate = min(maximum_size/self._height, maximum_size/self._width)
        yuki_width = self._width*yuki_rate
        yuki_height = self._height*yuki_rate
        return self._pixbuf.scale_simple(yuki_width, yuki_height, INTERP_TYPE)

    def __init__(self, path):
        self._pixbuf = GdkPixbuf.Pixbuf.new_from_file(path)
        self._width = self._pixbuf.get_width()
        self._height = self._pixbuf.get_height()
