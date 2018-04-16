
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatotext.eventbox.ForGrid import NagatoEventBox
from libnagatotext.dialog.WarningQuit import NagatoWarningQuit
from libnagatotext.Config import NagatoConfig


class NagatoMainWindow(NagatoObject, Gtk.Window):

    def _inform_config(self, user_data):
        yuki_group, yuki_key = user_data
        return self._config[yuki_group][yuki_key]

    def _yuki_n_config(self, user_data):
        self._config.set_data(user_data)
        self.show_all()

    def _yuki_n_new_file(self, file_name):
        print(file_name)

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
