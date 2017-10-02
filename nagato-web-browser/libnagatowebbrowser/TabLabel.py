
from gi.repository import Gtk
from gi.repository import Gdk
from libnagatowebbrowser.CoreObject import NagatoObject
from libnagatowebbrowser.ButtonClose import NagatoButtonClose

class NagatoTabLabel(Gtk.Box, NagatoObject):

    def _initialize_label(self):
        self._label = Gtk.Label("YUKI.N > now loading...")
        self.pack_start(self._label, True, False, 0)

    def set_title(self, title):
        if title is not None:
            self._label.set_text(title)
            self.show_all()

    def __init__(self, parent):
        self._parent = parent
        Gtk.Box.__init__(self)
        self._initialize_label()
        NagatoButtonClose(self)
        self.show_all()
