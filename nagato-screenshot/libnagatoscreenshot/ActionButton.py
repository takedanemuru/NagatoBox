
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.util import CssProvider


class NagatoActionButton(NagatoObject, Gtk.Button):

    def _on_clicked(self, button):
        self._raise(self._message)

    def __init__(self, parent, x, y, label, message, css=None):
        self._parent = parent
        Gtk.Button.__init__(self)
        self.connect("clicked", self._on_clicked)
        self.set_label(label)
        self._message = message
        self._parent.attach(self, x, y, 1, 1)
        if css is not None:
            CssProvider.set_to_widget(self, css)            
