
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoWindow(NagatoObject):

    def save_window_position(self, gtk_window):
        yuki_left, yuki_top = gtk_window.get_position()
        yuki_width, yuki_height = gtk_window.get_size()
        self._parent["window"]["x"] = str(yuki_left)
        self._parent["window"]["y"] = str(yuki_top)
        self._parent["window"]["w"] = str(yuki_width)
        self._parent["window"]["h"] = str(yuki_height)
        self._raise("YUKI.N > config changed")

    def load_window_position(self, gtk_window):
        yuki_left = self._parent.getint("window", "x")
        yuki_top = self._parent.getint("window", "y")
        yuki_width = self._parent.getint("window", "w")
        yuki_height = self._parent.getint("window", "h")
        if 0 >= yuki_width:
            gtk_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        else:
            gtk_window.move(yuki_left, yuki_top)
            gtk_window.set_default_size(yuki_width, yuki_height)

    def __init__(self, parent):
        self._parent = parent
