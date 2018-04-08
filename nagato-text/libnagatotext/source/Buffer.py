
from pathlib import Path
from libnagatotext.Prime import NagatoPrime
from libnagatotext.source.StyleSchemeManager import NagatoStyleSchemeManager
from libnagatotext.source.LanguageManager import NagatoLanguageManager
from libnagatotext.source.Clipboard import NagatoClipboard
from libnagatotext.FileHandler import NagatoFileHandler


class NagatoBuffer(NagatoPrime):

    def _yuki_n_clear_text(self):
        self._buffer.set_text("")

    def _yuki_n_set_text(self, path):
        yuki_path = Path(path)
        self._buffer.set_text(yuki_path.read_text())
        self._language_manager.guess(path)

    def _yuki_n_save_text(self, path):
        yuki_path = Path(path)
        yuki_path.write_text(self._buffer.get_property("text"))
        self._language_manager.guess(path)

    def _yuki_n_language_changed(self, language):
        self._buffer.set_language(language)

    def clipboard(self, command):
        self._clipboard(command)        

    def set_scheme(self, scheme):
        self._style_manager.set_scheme(scheme)

    def __init__(self, parent):
        self._parent = parent
        self._buffer = self._parent.get_buffer()
        self._clipboard = NagatoClipboard(self._buffer)
        self._language_manager = NagatoLanguageManager(self)
        self._style_manager = NagatoStyleSchemeManager(self, self._buffer)
        self._prime_object = NagatoFileHandler(self, self._buffer)
