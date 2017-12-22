
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from libnagatowebbrowser.CoreObject import NagatoObject
from libnagatowebbrowser.WebView import NagatoWebView
from libnagatowebbrowser.util.UniqueId import NagatoUniqueId
from libnagatowebbrowser.Notebook import NagatoNotebook

GRID_SPACING = 16


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_column_homogeneous(True)
        self.set_border_width(GRID_SPACING)
        self.set_row_spacing(GRID_SPACING)
        self.set_column_spacing(GRID_SPACING)

    def __init__(self, parent):
        self._id = NagatoUniqueId()
        self._initialize_grid()
        self._parent = parent
        self._parent.add(self)
        self._notebook = NagatoNotebook(self)
