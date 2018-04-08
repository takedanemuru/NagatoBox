
from gi.repository import Gtk
from gi.repository import Gdk


class NagatoClipboard(object):

    def __call__(self, command):
        if command == "cut":
            self._buffer.cut_clipboard(self._clipboard, True)
        if command == "copy":
            self._buffer.copy_clipboard(self._clipboard)
        if command == "paste":
            self._buffer.paste_clipboard(self._clipboard, None, True)

    def __init__(self, parent_buffer):
        self._buffer = parent_buffer
        yuki_display = Gdk.Display.get_default()
        self._clipboard = Gtk.Clipboard.get_default(yuki_display)
