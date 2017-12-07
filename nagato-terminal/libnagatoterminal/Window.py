
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.Grid2 import NagatoGrid
from libnagatoterminal.Dialog import NagatoDialog
from libnagatoterminal.AboutDialog2 import NagatoAboutDialog2
from libnagatoterminal.DBusServiceObject import NagatoDBusServiceObject
from libnagatoterminal.GdkX11Window import NagatoGdkX11Window
from libnagatoterminal.WindowAttributes import NagatoWindowAttributes

class NagatoWindow(Gtk.Window, NagatoObject):

    def _can_close(self):
        yuki_processes = self._grid.get_current_processes()
        if len(yuki_processes) == 0:
            return True
        else:
            yuki_dialog = NagatoDialog()
            yuki_response = yuki_dialog.run()
            yuki_dialog.destroy()
            return (yuki_response == Gtk.ResponseType.OK)

    def _try_quit_application(self):
        if self._can_close():
            self._attributes.save_window_positions()
            Gtk.main_quit()
            return False
        return True

    def _on_close_window(self, widget, event, user_data=None):
        return self._try_quit_application()

    def _yuki_n_quit(self):
        self._try_quit_application()

    def _yuki_n_about(self):
        yuki_dialog = NagatoAboutDialog2()
        yuki_dialog.run()
        yuki_dialog.destroy()

    def _yuki_n_move_to_current_desktop(self):
        yuki_gdk_window = NagatoGdkX11Window(self)
        yuki_gdk_window.move_to_current_desktop()

    def _initialize_window(self):
        Gtk.Window.__init__(self)
        self.connect("delete-event", self._on_close_window)
        self._attributes = NagatoWindowAttributes(self)

    def __init__(self):
        self._parent = None
        self._initialize_window()
        NagatoDialog.set_default_window(self)
        self._dbus = NagatoDBusServiceObject(self)
        self._grid = NagatoGrid(self)
        self.show_all()
        Gtk.main()
