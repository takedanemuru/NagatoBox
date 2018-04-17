
from gi.repository import GtkSource
from libnagato.Object import NagatoObject


class NagatoStyleSchemeManager(NagatoObject):

    def set_scheme(self, scheme):
        yuki_style = self._style_scheme_manager.get_scheme(scheme)
        self._buffer.set_style_scheme(yuki_style)

    def __init__(self, parent, text_buffer):
        self._parent = parent
        self._buffer = text_buffer
        self._style_scheme_manager = GtkSource.StyleSchemeManager.get_default()
        self.set_scheme("oblivion")
