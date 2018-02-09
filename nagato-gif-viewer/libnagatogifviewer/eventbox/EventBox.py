
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoEventBox(Gtk.EventBox, NagatoObject):

    def _on_initialize(self):
        pass

    def __init__(self, parent):
        self._parent = parent
        Gtk.EventBox.__init__(self)
        self._on_initialize()
