
from gi.repository import Gtk
from gi.repository import Gdk
from libnagato.Object import NagatoObject
from libnagatowebbrowser.Label import NagatoLabel


class NagatoNotebookTab(Gtk.Box, NagatoObject):

    def _initialize_label(self):
        self._label = NagatoLabel(self)
        self._label.set_property("has-tooltip", True)
        self.set_size_request(400, -1)
        self.pack_start(self._label, True, True, 0)

    def set_title(self, title):
        if title is not None:
            self._label.set_text(title)
            self._label.set_tooltip_text(title)
            self.show_all()

    def set_tab_size(self, new_tab_size):
        if 0>= new_tab_size:
            return
        self.set_size_request(new_tab_size, -1)
        
    def set_progress(self, progress):
        yuki_text = "YUKI.N > now loading... {:.0%}".format(progress)
        self._label.set_text(yuki_text)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Box.__init__(self)
        self._initialize_label()
        self.show_all()
