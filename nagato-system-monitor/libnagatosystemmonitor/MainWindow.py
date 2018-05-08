
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.dialog.message.Warning import NagatoWarning
from libnagato.ui.WindowAttributes import NagatoWindowAttributes
from libnagatosystemmonitor import Messages
from libnagatosystemmonitor.eventbox.ForGrid import NagatoEventBox

BUTTONS = ["Cancel", "Close"]


class NagatoMainWindow(NagatoObject, Gtk.Window):

    def _yuki_n_quit(self):
        self.close()

    def _on_close_window(self, widget, event, user_data=None):
        if NagatoWarning.call(message=Messages.QUIT, buttons=BUTTONS) == 0:
            return True
        return self._quit_main()

    def _quit_main(self):
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
