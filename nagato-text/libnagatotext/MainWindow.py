
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatotext.eventbox.ForGrid import NagatoEventBox
from libnagatotext.dialog.WarningQuit import NagatoWarningQuit
from libnagatotext.Config import NagatoConfig


class NagatoMainWindow(NagatoObject, Gtk.Window):

    def _yuki_n_quit(self):
        self.close()

    def _on_close_window(self, widget, event, user_data=None):
        if not NagatoWarningQuit.call():
            return True
        self._config.save_window_position(self)
        Gtk.main_quit()
        return False

    def _initialize_window(self):
        Gtk.Window.__init__(self)
        self._config.setup_window(self)
        self.connect("delete-event", self._on_close_window)

    def _on_initialize(self):
        NagatoEventBox(self)

    def __init__(self, parent):
        self._parent = parent
        self._config = NagatoConfig(self)
        self._initialize_window()
        self._on_initialize()
        self.show_all()
        Gtk.main()