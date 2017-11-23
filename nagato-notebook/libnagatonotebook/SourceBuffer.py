
from gi.repository import GtkSource
from libnagatonotebook.CoreObject import NagatoObject


class NagatoSourceBuffer(NagatoObject):

    def _on_changed(self, text_buffer):
        self._raise("YUKI.N > buffer changed")

    def _set_default_scheme(self):
        yuki_scheme = self._scheme_manager.get_scheme("codezone")
        self._buffer.set_style_scheme(yuki_scheme)

    def _set_default_language(self):
        self._language_manager = GtkSource.LanguageManager.get_default()
        yuki_language = self._language_manager.get_language("python3")
        self._buffer.set_language(yuki_language)

    def guess_language(self, path_to_file):
        yuki_language = self._language_manager.guess_language(
            path_to_file,
            None
            )
        self._buffer.set_language(yuki_language)

    def get_text(self):
        return self._buffer.get_property("text")

    def set_text(self, text):
        self._buffer.set_property("text", text)

    def __init__(self, parent, source_view):
        self._parent = parent
        self._buffer = source_view.get_buffer()
        self._buffer.connect("changed", self._on_changed)
        self._buffer.set_highlight_syntax(True)
        self._scheme_manager = GtkSource.StyleSchemeManager.get_default()
        self._set_default_scheme()
        self._set_default_language()
