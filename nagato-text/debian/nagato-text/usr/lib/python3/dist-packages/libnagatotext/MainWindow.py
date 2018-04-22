
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatotext.eventbox.ForGrid import NagatoEventBox
from libnagatotext.dialog.Warning2 import NagatoWarning2
from libnagatotext.dialog import Messages
from libnagatotext.WindowAttributes import NagatoWindowAttributes

MESSAGE = Messages.QUIT
BUTTONS = ["Cancel", "Close"]


class NagatoMainWindow(NagatoObject, Gtk.Window):

    def _yuki_n_new_file(self, file_name=None):
        if file_name is not None:
            self.set_title(file_name)
        else:
            self.set_title("nagato-text")

    def _yuki_n_quit(self):
        self.close()

    def _on_close_window(self, widget, event, user_data=None):
        if NagatoWarning2.call(message=MESSAGE, buttons=BUTTONS) == 0:
            return True
        self._attributes.save_window_position()
        Gtk.main_quit()
        return False

    def _initialize_window(self):
        Gtk.Window.__init__(self)
        self._attributes = NagatoWindowAttributes(self)
        self.connect("delete-event", self._on_close_window)

    def _on_initialize(self):
        NagatoEventBox(self)

    def __init__(self, parent):
        self._parent = parent
        self._initialize_window()
        self._on_initialize()
        self.show_all()
        Gtk.main()
