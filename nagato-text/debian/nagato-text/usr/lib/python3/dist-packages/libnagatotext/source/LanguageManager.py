
from gi.repository import GtkSource
from libnagato.Object import NagatoObject


class NagatoLanguageManager(NagatoObject):

    def guess(self, path):
        yuki_language = self._language_manager.guess_language(path)
        if yuki_language is not None:
            self._buffer.set_language(yuki_language)

    def __init__(self, text_buffer):
        self._buffer = text_buffer
        self._language_manager = GtkSource.LanguageManager.get_default()
