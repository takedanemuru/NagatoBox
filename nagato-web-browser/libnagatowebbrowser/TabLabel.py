
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Pango
from libnagatowebbrowser.CoreObject import NagatoObject
#from libnagatowebbrowser.ButtonClose import NagatoButtonClose
from libnagatowebbrowser.util.EllipsisedText import NagatoEllipsesedText


class NagatoTabLabel(Gtk.Box, NagatoObject):

    def _initialize_label(self):
        self._label = Gtk.Label("YUKI.N > now loading...")
        self.pack_start(self._label, True, False, 0)

    def set_title(self, title):
        if title is not None:
            self._label.set_text(self._ellipsised_text.get(title))
            self.show_all()

    def __init__(self, parent):
        self._parent = parent
        Gtk.Box.__init__(self)
        self._initialize_label()
        #NagatoButtonClose(self)
        self._ellipsised_text = NagatoEllipsesedText() 
        self.show_all()
