
import mimetypes
from pathlib import Path
from libnagato.Object import NagatoObject


class NagatoPaths(NagatoObject):

    def _is_image_path(self, path):
        yuki_mime, yuki_encode = mimetypes.guess_type(path)
        if yuki_mime is None:
            return False
        return yuki_mime.startswith("image")

    def _reset_paths(self, directory):
        self._directory = directory
        self._paths = []
        for yuki_path in Path(directory).iterdir():
            if self._is_image_path(yuki_path.as_posix()):
                self._paths.append(yuki_path.as_posix())

    def reset_paths(self, path):
        self._reset_paths(Path(path).parent.as_posix())
        return self._paths.index(path)

    def __getitem__(self, index):
        return self._paths[index]

    def __init__(self, parent):
        self._parent = parent
        self._reset_paths(Path.home().as_posix())

    @property
    def maximum(self):
        return len(self._paths)

    @property
    def directory(self):
        return self._directory
