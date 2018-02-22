
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.util import CssProvider

HEIGHT = 48


class NagatoBox(NagatoObject, Gtk.Box):

    def _on_initialize(self, user_data=None):
        # YOU MUST OVERRIDE THIS METHOD
        pass

    def _on_set_size(self):
        self.set_size_request(-1, HEIGHT)
        self.set_homogeneous(True)
        self.set_hexpand(True)

    def _on_set_css(self):
        CssProvider.set_to_widget(self, "shade-full")

    def __init__(self, parent, user_data=None):
        self._parent = parent
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self._on_set_css()
        self._on_set_size()
        self._on_initialize(user_data)
