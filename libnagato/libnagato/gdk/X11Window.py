

from gi.repository import Gdk
from gi.repository import GdkX11

STATE_FULLSCREEN = Gdk.WindowState.FULLSCREEN


class NagatoX11Window(object):

    def is_fullscreen(self):
        # yuki_state is bitmap-mask.
        # see gdk reference for more detail.
        yuki_state = self._gdk_window.get_state()
        return (yuki_state & STATE_FULLSCREEN == STATE_FULLSCREEN)

    def toggle_fullscreen(self):
        if self.is_fullscreen()
            self._gtk_window.unfullscreen()
        else:
            self._gtk_window.fullscreen()

    def move_to_current_desktop(self):
        self._gdk_x11_window.move_to_current_desktop()

    def __init__(self, gtk_window):
        self._gtk_window = gtk_window
        self._gdk_window = gtk_window.get_window()
        self._gdk_x11_window = GdkX11.X11Window.lookup_for_display(
            Gdk.Display.get_default(),
            self._gdk_window.get_xid()
            )
