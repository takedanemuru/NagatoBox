
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoWindow(Gtk.Window, NagatoObject):

    def __init__(self, parent):
        self._parent = parent
        Gtk.Window.__init__(self)
        self.set_default_size(600, 300)
