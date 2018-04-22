
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.Ux import Unit


class NagatoWindowAttributes(NagatoObject):

    def _move(self, allocation):
        self._parent.set_default_size(allocation["w"], allocation["h"])
        self._parent.move(allocation["x"], allocation["y"])

    def _set_default(self, allocation):
        yuki_width = Unit(allocation["w"])
        yuki_height = Unit(allocation["h"])
        self._parent.set_default_size(yuki_width, yuki_height)
        self._parent.set_position(Gtk.WindowPosition.CENTER_ALWAYS)

    def _load_window_position(self):
        yuki_data = "window", "allocation"
        yuki_config = self._enquiry("YUKI.N > config", yuki_data)
        yuki_allocation = eval(yuki_config)
        if isinstance(yuki_allocation["w"], str):
            self._set_default(yuki_allocation)
        else:
            self._move(yuki_allocation)
        self._parent.unfullscreen()

    def _set_application_icon(self):
        yuki_icon_pixbuf = self._enquiry("YUKI.N > pixbuf", "application.png")
        self._parent.set_icon(yuki_icon_pixbuf)

    def save_window_position(self):
        yuki_x, yuki_y = self._parent.get_position()
        yuki_w, yuki_h = self._parent.get_size()
        yuki_allocation = {"x": yuki_x, "y": yuki_y, "w": yuki_w, "h": yuki_h}
        yuki_data = ("window", "allocation", yuki_allocation)
        self._raise("YUKI.N > config", yuki_data)

    def __init__(self, parent):
        self._parent = parent
        self._load_window_position()
        self._set_application_icon()
