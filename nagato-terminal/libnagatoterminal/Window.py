
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.Grid2 import NagatoGrid
from libnagatoterminal.DBusServiceObject import NagatoDBusServiceObject
from libnagatoterminal.GdkX11Window import NagatoGdkX11Window
from libnagatoterminal.WindowAttributes import NagatoWindowAttributes
from libnagatoterminal import DialogFacade


class NagatoWindow(Gtk.Window, NagatoObject):

    def _can_close(self):
        yuki_processes = self._grid.get_current_processes()
        return DialogFacade.get_can_close_window(yuki_processes)

    def _try_quit_application(self):
        if not self._can_close():
            return True
        self._attributes.save_window_positions()
        Gtk.main_quit()
        return False

    def _on_close_window(self, widget, event, user_data=None):
        # this method is GTK+ callback
        # cancels to close window when returns True
        return self._try_quit_application()

    def _yuki_n_quit(self):
        self._try_quit_application()

    def _yuki_n_about(self):
        DialogFacade.show_about()

    def _yuki_n_move_to_current_desktop(self):
        yuki_gdk_window = NagatoGdkX11Window(self)
        yuki_gdk_window.move_to_current_desktop()

    def _initialize_window(self):
        Gtk.Window.__init__(self)
        self.connect("delete-event", self._on_close_window)
        self._attributes = NagatoWindowAttributes(self)

    def __init__(self):
        # this object is the most top instance of NagatoObjects' CoC.
        # has no parent, nowhere to go up.
        self._parent = None
        self._initialize_window()
        DialogFacade.set_default_window(self)
        NagatoDBusServiceObject(self)
        self._grid = NagatoGrid(self)
        self.show_all()
        Gtk.main()
