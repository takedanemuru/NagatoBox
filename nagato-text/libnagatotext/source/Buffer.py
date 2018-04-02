
from libnagato.Object import NagatoObject
from libnagatotext.source.StyleSchemeManager import NagatoStyleSchemeManager
from libnagatotext.source.LanguageManager import NagatoLanguageManager
from libnagatotext.FileHandler import NagatoFileHandler


class NagatoBuffer(NagatoObject):

    def _yuki_n_clear_text(self):
        self._buffer.set_text("")

    def _yuki_n_set_text(self, path):
        with open(path, "r") as yuki_file:
            self._buffer.set_text(yuki_file.read())
            yuki_file.close()
        self._language_manager.guess(path)

    def _yuki_n_save_text(self, path):
        with open(path, "w") as yuki_file:
            yuki_file.write(self._buffer.get_property("text"))
            yuki_file.close()
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
