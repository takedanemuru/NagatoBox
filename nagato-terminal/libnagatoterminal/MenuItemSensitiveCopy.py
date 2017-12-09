
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject


class NagatoMenuItemSensitiveCopy(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        self._raise("YUKI.N > copy")

    def _on_draw(self, widget, cr):
        self.set_sensitive(self._enquiry("YUKI.N > has selection"))

    def __init__(self, parent):
        self._parent = parent
        Gtk.MenuItem.__init__(self, "Copy")
        self.connect("activate", self._on_activate)
        self.connect("draw", self._on_draw)
        self._parent.append(self)
