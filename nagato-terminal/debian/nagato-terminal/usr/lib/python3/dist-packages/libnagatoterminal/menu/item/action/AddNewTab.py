
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoAddNewTab(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        self._raise(
            "YUKI.N > add new tab",
            self._enquiry("YUKI.N > working directory")
            )

    def __init__(self, parent):
        self._parent = parent
        Gtk.MenuItem.__init__(self, "Add New Tab")
        self.connect("activate", self._on_activate)
        self._parent.append(self)
