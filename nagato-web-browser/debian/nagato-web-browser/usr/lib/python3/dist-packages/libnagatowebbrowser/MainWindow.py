import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from libnagatowebbrowser.Grid import NagatoGrid
from libnagatowebbrowser import CssProvider
from libnagatowebbrowser.CoreObject import NagatoObject
from libnagatowebbrowser import GdkPixbufIcon

class NagatoMainWindow(Gtk.Window, NagatoObject):

    def _yuki_n_current_page_load_finished(self, user_data):
        self.set_title(user_data[1])

    def _on_close_window(self, widget, event, user_data=None):
        Gtk.main_quit()

    def _initialize_window(self):
        Gtk.Window.__init__(self)
        self.set_default_size(800, 600)
        self.set_icon(GdkPixbufIcon.get_application_icon())
        self.connect("delete-event", self._on_close_window)

    def __init__(self):
        self._parent = None
        CssProvider.set_to_application()
        self._initialize_window()
        NagatoGrid(self)
        self.show_all()
        Gtk.main()