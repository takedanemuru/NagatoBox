
from gi.repository import GtkSource
from libnagato.Object import NagatoObject


class NagatoLanguageManager(NagatoObject):

    def guess(self, path):
        yuki_language = self._language_manager.guess_language(path)
        if yuki_language is not None:
            self._raise("YUKI.N > language changed", yuki_language)

    def __init__(self, parent):
        self._parent = parent
        self._language_manager = GtkSource.LanguageManager.get_default()
