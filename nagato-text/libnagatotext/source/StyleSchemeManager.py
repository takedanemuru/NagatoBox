
from gi.repository.GtkSource import StyleSchemeManager
from libnagato.Object import NagatoObject


class NagatoStyleSchemeManager(NagatoObject):

    def set_scheme(self, scheme):
        yuki_style = self._style_scheme_manager.get_scheme(scheme)
        self._buffer.set_style_scheme(yuki_style)

    def _set_first_scheme(self):
        yuki_data = "sourceview", "style_scheme"
        yuki_scheme = self._enquiry("YUKI.N > config", yuki_data)
        if yuki_scheme != "":
            self.set_scheme(yuki_scheme)

    def __init__(self, parent, text_buffer):
        self._parent = parent
        self._buffer = text_buffer
        self._style_scheme_manager = StyleSchemeManager.get_default()
        self._set_first_scheme()
