
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.gdk.X11Window import NagatoX11Window
from libnagatoterminal.dbus.ServiceObject import NagatoServiceObject
from libnagatoterminal.WindowAttributes import NagatoWindowAttributes
from libnagatoterminal.EventBoxForGrid import NagatoEventBox


class NagatoWindow(Gtk.Window, NagatoObject):

    def _try_quit_application(self):
        if not self._event_box.can_close():
            return True
        self._attributes.save_window_position()
        Gtk.main_quit()
        return False

    def _on_close_window(self, widget, event, user_data=None):
        return self._try_quit_application()

    def _yuki_n_quit(self):
        self._try_quit_application()

    def _yuki_n_move_to_current_desktop(self):
        yuki_gdk_window = NagatoX11Window(self)
        yuki_gdk_window.move_to_current_desktop()

    def _on_initialize(self):
        NagatoServiceObject(self)
        self._event_box = NagatoEventBox(self)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Window.__init__(self, Gtk.WindowType.TOPLEVEL)
        self.connect("delete-event", self._on_close_window)
        self._attributes = NagatoWindowAttributes(self)
        self._on_initialize()
        self.show_all()
        Gtk.main()
