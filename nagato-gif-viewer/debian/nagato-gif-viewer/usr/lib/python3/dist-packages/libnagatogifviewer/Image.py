
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from libnagato.Object import NagatoObject


class NagatoImage(Gtk.Image, NagatoObject):

    def _get_path(self):
        yuki_args = self._enquiry("YUKI.N > args")
        if yuki_args["path"] is not None:
            return yuki_args["path"]
        yuki_resources = self._enquiry("YUKI.N > resources")
        return yuki_resources.get_image_path("nagato.gif")        

    def __init__(self, parent):
        self._parent = parent
        Gtk.Image.__init__(self)
        self.set_hexpand(True)
        self.set_vexpand(True)
        yuki_path = self._get_path()
        yuki_animation = GdkPixbuf.PixbufAnimation.new_from_file(yuki_path)
        self.set_from_animation(yuki_animation)
        self._parent.add(self)
