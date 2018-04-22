
from pathlib import Path
from libnagato.Object import NagatoObject


class NagatoRecentPaths(NagatoObject):

    def _sanitize(self, paths):
        yuki_paths = []
        for yuki_path in paths:
            if not Path(yuki_path).exisists():
                continue
            yuki_paths.append(yuki_path)
        return yuki_paths

    def _get(self):
        yuki_paths = self._enquiry("YUKI.N > config", ("recent", "paths"))
        if yuki_paths == "":
            return None
        else:
            return self._sanitize(yuki_paths)

    def clear(self):
        self._raise("YUKI.N > config", ("recent", "paths", ""))

    def get(self):
        return self._get()

    def set(self, path):
        yuki_paths = self._get()
        if yuki_paths is None:
            self._raise("YUKI.N > config", ("recent", "paths", ""))
        else:
            pass

    def __init__(self, parent):
        self._parent = parent
