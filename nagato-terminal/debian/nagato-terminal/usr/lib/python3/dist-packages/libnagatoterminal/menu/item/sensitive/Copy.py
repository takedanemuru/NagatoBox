
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoCopy(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        self._raise("YUKI.N > copy")

    def _on_map(self, widget):
        self.set_sensitive(self._enquiry("YUKI.N > has selection"))

    def __init__(self, parent):
        self._parent = parent
        Gtk.MenuItem.__init__(self, "Copy")
        self.connect("activate", self._on_activate)
        self.connect("map", self._on_map)
        self._parent.append(self)
