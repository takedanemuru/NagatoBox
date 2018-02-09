
from gi.repository import Gtk
from libnagato.util import CssProvider
from libnagato.Object import NagatoObject

BORDER_WIDTH = 8


class NagatoButton(NagatoObject, Gtk.Button):

    def _on_clicked(self, button):
        self._raise(self._message)

    def _initialize_button(self, label, css=None):
        Gtk.Button.__init__(self)
        self.set_label(label)
        self.set_border_width(BORDER_WIDTH)
        self.connect("clicked", self._on_clicked)
        if css is not None:
            CssProvider.set_to_widget(self, css)

    def __init__(self, parent, label, message, css=None):
        self._parent = parent
        self._message = message
        self._initialize_button(label, css)
        self._parent.pack_start(self, False, True, 0)
