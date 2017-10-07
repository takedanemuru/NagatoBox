
from gi.repository import Gtk
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.SourceView import NagatoSourceView
from libnagatonotebook.BoxToolbar import NagatoBoxToolbar

class NagatoGrid(Gtk.Grid, NagatoObject):

    def __init__(self, parent):
        self._parent = parent
        Gtk.Grid.__init__(self)
        self._parent.add(self)
        self.set_border_width(16)
        self.set_row_spacing(16)
        self.set_hexpand(True)
        self.set_vexpand(True)
        self._toolbar = NagatoBoxToolbar(self)
        self._source_view = NagatoSourceView(self)
        self.show_all()
