
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject


class NagatoShrink(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        self._raise("YUKI.N > menu clicked", self._direction)

    def _on_map(self, widget):
        yuki_sensitive = self._enquiry(self._query, self._direction)
        self.set_sensitive(yuki_sensitive)

    def __init__(self, parent, title, gtk_position_type):
        self._parent = parent
        Gtk.MenuItem.__init__(self, title)
        self._query = "YUKI.N > can shrink to"
        self._direction = gtk_position_type
        self.connect("activate", self._on_activate)
        self.connect("map", self._on_map)
        self._parent.append(self)
