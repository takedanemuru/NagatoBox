
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.gdk.X11Window import NagatoX11Window
from libnagato.dialog.About import NagatoAboutDialog
from libnagatoterminal.Resources import NagatoResources
from libnagatoterminal.Grid import NagatoGrid
from libnagatoterminal.dbus.ServiceObject import NagatoServiceObject
from libnagatoterminal.WindowAttributes import NagatoWindowAttributes
from libnagatoterminal.menu.context.ForChrome import NagatoForChrome
from libnagatoterminal.dialog import Portal


class NagatoWindow(Gtk.Window, NagatoObject):

    def _can_close(self):
        yuki_processes = self._grid.get_current_processes()
        return Portal.get_can_close_window(yuki_processes)

    def _try_quit_application(self):
        if not self._can_close():
            return True
        self._attributes.save_window_positions()
        Gtk.main_quit()
        return False

    def _on_close_window(self, widget, event, user_data=None):
        # this method is GTK+ callback
        # cancels closing window event when it returns True
        return self._try_quit_application()

    def _yuki_n_quit(self):
        self._try_quit_application()

    def _yuki_n_about(self):
        yuki_dialog = NagatoAboutDialog(NagatoResources())
        yuki_dialog.run()
        yuki_dialog.destroy()

    def _yuki_n_move_to_current_desktop(self):
        yuki_gdk_window = NagatoX11Window(self)
        yuki_gdk_window.move_to_current_desktop()

    def _on_initialize(self):
        self._attributes = NagatoWindowAttributes(self)
        NagatoServiceObject(self)
        self._grid = NagatoGrid(self)
        NagatoForChrome(self)

    def __init__(self):
        # this object is the most top instance of NagatoObjects' CoC.
        # has no parent, nowhere to go up.
        self._parent = None
        Gtk.Window.__init__(self, Gtk.WindowType.TOPLEVEL)
        self.connect("delete-event", self._on_close_window)
        self._on_initialize()
        self.show_all()
        Gtk.main()
