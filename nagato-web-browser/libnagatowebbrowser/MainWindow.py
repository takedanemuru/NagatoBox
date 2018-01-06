import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import Gdk
from libnagato.Object import NagatoObject
from libnagato.dialog.About import NagatoAboutDialog
from libnagatowebbrowser.Resources import NagatoResources
from libnagatowebbrowser.Grid import NagatoGrid

STATE_FULLSCREEN = Gdk.WindowState.FULLSCREEN


class NagatoMainWindow(Gtk.Window, NagatoObject):

    def _yuki_n_new_title(self, title=None):
        if title is not None:
            self.set_title(title)

    def _yuki_n_toggle_fullscreen(self):
        if self._is_fullscreen():
            self.unfullscreen()
        else:
            self.fullscreen()

    def _yuki_n_about(self):
        yuki_dialog = NagatoAboutDialog(NagatoResources())
        yuki_dialog.run()
        yuki_dialog.destroy()

    def _yuki_n_quit(self):
        Gtk.main_quit()

    def _inform_main_window_itself(self):
        return self

    def _inform_is_fullscreen(self):
        return self._is_fullscreen()

    def _is_fullscreen(self):
        yuki_gdk_window = self.get_window()
        yuki_state = yuki_gdk_window.get_state()
        return (yuki_state & STATE_FULLSCREEN == STATE_FULLSCREEN)

    def _on_close_window(self, widget, event, user_data=None):
        Gtk.main_quit()

    def _on_initialize(self):
        Gtk.Window.__init__(self)
        self.set_default_size(800, 600)
        self.connect("delete-event", self._on_close_window)
        NagatoGrid(self)

    def __init__(self):
        self._parent = None
        self._on_initialize()
        self.show_all()
        Gtk.main()
