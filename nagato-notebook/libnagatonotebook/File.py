
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.DialogSaveFile import NagatoDialogSaveFile
from libnagatonotebook.SourceBuffer import NagatoSourceBuffer


class NagatoFile(NagatoObject):

    def _is_file_closable(self):
        if self._saved:
            return True
        return False

    def _save_file_to(self, path_to_save):
        self._saved = True
        self._path = path_to_save
        with open(path_to_save, mode="w") as yuki_file:
            yuki_file.write(self._buffer.get_text())

    def _yuki_n_buffer_changed(self):
        self._saved = False

    def _request_path_new(self):
        if self._saved:
            self._raise("YUKI.N > path new", self._path)
            self._buffer.guess_language(self._path)

    def save(self):
        if self._saved:
            return
        elif self._path != "":
            self._save_file_to(self._path)
            self._request_path_new()
        else:
            self.save_as()

    def save_as(self):
        yuki_path, yuki_resonse = self._dialog_save_file.save_file()
        if yuki_path is not None:
            self._save_file_to(yuki_path)
            self._request_path_new()
 
    def set_file(self, path_to_file):
        with open(path_to_file, mode="r") as yuki_file:
            self._buffer.set_text(yuki_file.read())
            self._path = path_to_file
            self._saved = True
            self._request_path_new()

    def get_path(self):
        return self._path

    def __init__(self, parent):
        self._parent = parent
        self._buffer = NagatoSourceBuffer(self, self._parent)
        self._path = ""
        self._saved = True
        self._dialog_save_file = NagatoDialogSaveFile()
