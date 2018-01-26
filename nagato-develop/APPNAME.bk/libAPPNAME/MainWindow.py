import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.dialog.About import NagatoAboutDialog
from libAPPNAME.eventbox.ForGrid import NagatoEventBox
from libAPPNAME.dialog.WarningQuit import NagatoWarningQuit


class NagatoMainWindow(NagatoObject, Gtk.Window):

    def _yuki_n_about(self):
        NagatoAboutDialog.call(self._resources)

    def _yuki_n_quit(self):
        self.close()

    def _on_close_window(self, widget, event, user_data=None):
        if not NagatoWarningQuit.call():
            return True
        Gtk.main_quit()
        return False

    def _on_initialize(self):
        Gtk.Window.__init__(self)
        self.set_default_size(800, 600)
        self.set_icon(self._resources.get_application_icon())
        self.connect("delete-event", self._on_close_window)
        NagatoEventBox(self)

    def __init__(self, resources):
        self._parent = None
        self._resources = resources
        self._on_initialize()
        self.show_all()
        Gtk.main()
