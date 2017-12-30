
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoAddNewTab(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        yuki_sensitive = self._enquiry("YUKI.N > working directory")
        self._raise("YUKI.N > add new tab", yuki_sensitive)

    def __init__(self, parent):
        self._parent = parent
        Gtk.MenuItem.__init__(self, "Add New Tab")
        self.connect("activate", self._on_activate)
        self._parent.append(self)
