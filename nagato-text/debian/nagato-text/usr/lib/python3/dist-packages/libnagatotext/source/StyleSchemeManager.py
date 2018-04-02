
from gi.repository import GtkSource
from libnagato.Object import NagatoObject


class NagatoStyleSchemeManager(NagatoObject):

    def __init__(self, parent, text_buffer):
        self._parent = parent
        self._style_scheme_manager = GtkSource.StyleSchemeManager.get_default()
        yuki_style = self._style_scheme_manager.get_scheme("oblivion")
        text_buffer.set_style_scheme(yuki_style)
