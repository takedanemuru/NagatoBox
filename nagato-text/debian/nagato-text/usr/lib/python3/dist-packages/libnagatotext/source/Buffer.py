
from pathlib import Path
from libnagato.Object import NagatoObject
from libnagatotext.source.StyleSchemeManager import NagatoStyleSchemeManager
from libnagatotext.source.LanguageManager import NagatoLanguageManager
from libnagatotext.FileHandler import NagatoFileHandler


class NagatoBuffer(NagatoObject):

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

    def new(self):
        self._file_handler.new()

    def load(self):
        self._file_handler.load()

    def save(self):
        self._file_handler.save()

    def save_as(self):
        self._file_handler.save_as()

    def __init__(self, parent):
        self._parent = parent
        self._buffer = self._parent.get_buffer()
        self._language_manager = NagatoLanguageManager(self)
        NagatoStyleSchemeManager(self, self._buffer)
        self._file_handler = NagatoFileHandler(self, self._buffer)
