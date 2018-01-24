import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.gdk.X11Window import NagatoX11Window
from libnagato.dialog.About import NagatoAboutDialog
from libnagatowebbrowser.Resources import NagatoResources
from libnagatowebbrowser.Grid import NagatoGrid
from libnagatowebbrowser.EventBoxForGrid import NagatoEventBox

class NagatoMainWindow(Gtk.Window, NagatoObject):

    def _yuki_n_new_title(self, title=None):
        if title is not None:
            self.set_title(title)

    def _yuki_n_toggle_fullscreen(self):
        self._x11_window.toggle_fullscreen()

    def _yuki_n_about(self):
        NagatoAboutDialog.call(NagatoResources())

    def _yuki_n_quit(self):
        Gtk.main_quit()

    def _inform_main_window_itself(self):
        return self

    def _inform_is_fullscreen(self):
        return self._x11_window.is_fullscreen()

    def _on_close_window(self, widget, event, user_data=None):
        Gtk.main_quit()

    def _on_initialize(self):
        Gtk.Window.__init__(self)
        self.set_default_size(800, 600)
        self.set_icon(NagatoResources().get_application_icon())
        self.connect("delete-event", self._on_close_window)

    def __init__(self):
        self._parent = None
        self._on_initialize()
        self._event_box = NagatoEventBox(self)
        # X11 window cannot get x11id before it's shown.
        self.show_all()
        self._x11_window = NagatoX11Window(self)
        Gtk.main()
