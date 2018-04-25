
from gi.repository import Gtk
from libnagatotext.source.View import NagatoView
from libnagatotext.Prime import NagatoPrime


class NagatoScrolledWindow(Gtk.ScrolledWindow, NagatoPrime):

    def __init__(self, parent):
        self._parent = parent
        Gtk.ScrolledWindow.__init__(self)
        self.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.set_vexpand(True)
        self.set_hexpand(True)
        self._prime_object = NagatoView(self)
