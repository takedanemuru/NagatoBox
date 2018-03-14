
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.dialog.About import NagatoAboutDialog
from libnagatoscreenshot.eventbox.ForGrid import NagatoEventBox
from libnagatoscreenshot.dialog.WarningQuit import NagatoWarningQuit
from libnagatoscreenshot.Config import NagatoConfig


class NagatoMainWindow(NagatoObject, Gtk.Window):

    def _yuki_n_about(self):
        NagatoAboutDialog.call(self._resources)

    def _yuki_n_quit(self):
        self.close()

    def _on_close_window(self, widget, event, user_data=None):
        #if not NagatoWarningQuit.call():
        #    return True
        self._config.save_window_position(self)
        Gtk.main_quit()
        return False

    def _initialize_window(self):
        Gtk.Window.__init__(self)
        self.set_default_size(640, 320)
        self._config.load_window_position(self)
        self.set_icon(self._resources.get_application_icon())
        self.connect("delete-event", self._on_close_window)

    def _on_initialize(self):
        NagatoEventBox(self)

    def __init__(self, parent, args, resources):
        self._parent = parent
        self._args = args
        self._resources = resources
        self._config = NagatoConfig(self._resources.get_config_file())
        self._initialize_window()
        self._on_initialize()
        self.show_all()
        Gtk.main()
