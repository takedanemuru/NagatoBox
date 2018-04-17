
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoWindowAttributes(NagatoObject):

    def _move(self, allocation):
        self._parent.move(allocation["x"], allocation["y"])
        self._parent.set_default_size(allocation["w"], allocation["h"])

    def _load_window_position(self):
        yuki_data = ("window", "allocation")
        yuki_config = self._enquiry("YUKI.N > config", yuki_data)
        yuki_allocation = eval(yuki_config)
        if 0 >= yuki_allocation["w"]:
            self._parent.set_default_size(800, 640)
            self._parent.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        else:
            self._move(yuki_allocation)
        self._parent.unfullscreen()

    def _set_application_icon(self):
        yuki_icon_pixbuf = self._enquiry("YUKI.N > pixbuf", "application.png")
        self._parent.set_icon(yuki_icon_pixbuf)

    def save_window_position(self):
        yuki_x, yuki_y = self._parent.get_position()
        yuki_w, yuki_h = self._parent.get_size()
        yuki_allocation = {"x":yuki_x, "y":yuki_y, "w":yuki_w, "h":yuki_h}
        yuki_data = ("window", "allocation", yuki_allocation)
        self._raise("YUKI.N > save config", yuki_data)

    def __init__(self, parent):
        self._parent = parent
        self._load_window_position()
        self._set_application_icon()
