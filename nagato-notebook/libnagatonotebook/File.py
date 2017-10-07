
import os
from gi.repository import Gtk
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.DialogSaveFile import NagatoDialogSaveFile


class NagatoFile(NagatoObject):

    def _is_file_closable(self):
        if self._saved:
            return True
        return Ture

    def _save_file_to(self, path_to_save):
        self._saved = True
        self._path = path_to_save
        yuki_file = open(path_to_save, "w")
        yuki_file.write(self._text_buffer.text)

    def save(self):
        if self._saved:
            pass
        elif self._path != "":
            self._save_file_to(self._path)
        else:
            yuki_path = self._dialog_save_file.save_file()
            print(yuki_path)
            if yuki_path is None:
                return False
        return self._saved

    def _on_changed(self, text_buffer):
        self._saved = False

    def __init__(self, parent):
        self._parent = parent
        self._text_buffer = self._parent.get_buffer()
        self._text_buffer.connect("changed", self._on_changed)
        self._path = ""
        self._saved = True
        self._dialog_save_file = NagatoDialogSaveFile()
