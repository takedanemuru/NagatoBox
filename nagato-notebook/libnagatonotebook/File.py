
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.DialogSaveFile import NagatoDialogSaveFile


class NagatoFile(NagatoObject):

    def _is_file_closable(self):
        if self._saved:
            return True
        return False

    def _save_file_to(self, path_to_save):
        self._saved = True
        self._path = path_to_save
        with open(path_to_save, mode="w") as yuki_file:
            yuki_file.write(self._text_buffer.get_property("text"))

    def _on_changed(self, text_buffer):
        self._saved = False

    def save(self):
        if self._saved:
            pass
        elif self._path != "":
            self._save_file_to(self._path)
        else:
            return self.save_as()
        return self._saved

    def save_as(self):
        yuki_path = self._dialog_save_file.save_file()
        if yuki_path is None:
            return False
        self._save_file_to(yuki_path)
        return self._saved

    def set_file(self, path_to_file):
        with open(path_to_file, mode="r") as yuki_file:
            self._text_buffer.set_property("text", yuki_file.read())
            self._path = path_to_file
            self._saved = True

    def __init__(self, parent):
        self._parent = parent
        self._text_buffer = self._parent.get_buffer()
        self._text_buffer.connect("changed", self._on_changed)
        self._path = ""
        self._saved = True
        self._dialog_save_file = NagatoDialogSaveFile()
