
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.dialog.About import NagatoAboutDialog
from libnagatogifviewer.eventbox.ForGrid import NagatoEventBox
from libnagatogifviewer.dialog.WarningQuit import NagatoWarningQuit
from libnagatogifviewer.Config import NagatoConfig


class NagatoMainWindow(NagatoObject, Gtk.Window):

    def _yuki_n_about(self):
        NagatoAboutDialog.call(self._resources)

    def _yuki_n_quit(self):
        self.close()

    def _on_close_window(self, widget, event, user_data=None):
        self._config.save_window_position(self)
        Gtk.main_quit()

    def _initialize_window(self):
        Gtk.Window.__init__(self)
        self.set_default_size(100, 100)
        self._config.load_window_position(self)
        self.set_icon(self._resources.get_application_icon())
        self.connect("delete-event", self._on_close_window)

    def _on_initialize(self):
        NagatoEventBox(self)

    def __init__(self, args, resources):
        self._parent = None
        self._args = args
        self._resources = resources
        self._config = NagatoConfig(self._resources.get_config_file())
        self._initialize_window()
        self._on_initialize()
        self.show_all()
        Gtk.main()
