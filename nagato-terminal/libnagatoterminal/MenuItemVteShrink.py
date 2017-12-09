from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject


class NagatoMenuItemVteShrink(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        self._raise("YUKI.N > menu clicked", self._direction)

    def _on_draw(self, widget, cr):
        yuki_sensitive = self._enquiry(self._query, self._direction)
        self.set_sensitive(yuki_sensitive)        

    def __init__(self, parent, title, gtk_position_type):
        self._parent = parent
        Gtk.MenuItem.__init__(self, title)
        self._query = "YUKI.N > can shrink to"
        self._direction = gtk_position_type
        self.connect("activate", self._on_activate)
        self.connect("draw", self._on_draw)
        self._parent.append(self)        

