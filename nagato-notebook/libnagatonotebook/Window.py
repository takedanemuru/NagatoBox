
import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from libnagatonotebook.SourceView import NagatoSourceView


class NagatoWindow(Gtk.Window):

    def _on_destroy(self, widget, event, user_data=None):
        Gtk.main_quit()

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(600, 400)
        self.connect("delete-event", self._on_destroy)
        self.set_border_width(16)
        NagatoSourceView(self)
        self.show_all()
        Gtk.main()
