
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoItemRight(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        self._raise(self._message, self._user_data)

    def __init__(self, parent, label, message, user_data=None):
        self._parent = parent
        Gtk.MenuItem.__init__(self, label)
        self.connect("activate", self._on_activate)
        self.set_halign(1)
        self.set_hexpand(True)
        self._message = message
        self._user_data = user_data
        self._parent.append(self)
