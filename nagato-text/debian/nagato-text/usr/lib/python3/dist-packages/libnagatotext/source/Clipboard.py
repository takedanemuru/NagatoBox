
from gi.repository import Gtk
from gi.repository import Gdk


class NagatoClipboard(object):

    def _command_cut(self):
        self._buffer.cut_clipboard(self._clipboard, True)

    def _command_paste(self):
        self._buffer.paste_clipboard(self._clipboard, None, True)

    def _command_copy(self):
        self._buffer.copy_clipboard(self._clipboard)

    def __call__(self, command):
        yuki_method = getattr(self, "_command_{}".format(command))
        yuki_method()

    def __init__(self, parent_buffer):
        self._buffer = parent_buffer
        yuki_display = Gdk.Display.get_default()
        self._clipboard = Gtk.Clipboard.get_default(yuki_display)
