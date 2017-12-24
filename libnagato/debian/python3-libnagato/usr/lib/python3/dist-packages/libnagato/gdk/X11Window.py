
from gi.repository import Gdk
from gi.repository import GdkX11


class NagatoX11Window(object):

    def move_to_current_desktop(self):
        self._gdk_window.move_to_current_desktop()

    def __init__(self, gtk_window):
        yuki_xid = gtk_window.get_window().get_xid()
        self._gdk_window = GdkX11.X11Window.lookup_for_display(
            Gdk.Display.get_default(),
            yuki_xid
            )
