import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from libnagatowebbrowser.CoreObject import NagatoObject
from libnagatowebbrowser.WebView import NagatoWebView
from libnagatowebbrowser.util.UniqueId import NagatoUniqueId
from libnagatowebbrowser.Notebook import NagatoNotebook
from libnagatowebbrowser.ToolBar import NagatoToolBar

GRID_SPACING = 16


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _yuki_n_current_page_load_finished(self, user_data):
        self._tool_bar.set_uri(user_data[2])
        self._raise("YUKI.N > current page load finished", user_data)

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
        self._tool_bar = NagatoToolBar(self)
        self._notebook = NagatoNotebook(self)
