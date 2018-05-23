
from gi.repository import Gtk
from libnagato.Ux import Unit
from libnagatoimageviewer.ui.DrawingArea import NagatoDrawingArea
from libnagatoimageviewer.Prime import NagatoPrime


class NagatoScrolledWindow(Gtk.ScrolledWindow, NagatoPrime):

    def __init__(self, parent):
        self._parent = parent
        Gtk.ScrolledWindow.__init__(self)
        self.set_hexpand(True)
        self.set_vexpand(True)
        self.set_property("margin-left", Unit("grid-spacing"))
        self.set_property("margin-right", Unit("grid-spacing"))
        self.set_property("margin-top", Unit("grid-spacing"))
        self._prime_object = NagatoDrawingArea(self)        
