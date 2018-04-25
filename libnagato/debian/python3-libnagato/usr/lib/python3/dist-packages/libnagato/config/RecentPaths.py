
from pathlib import Path
from libnagato.Object import NagatoObject


class NagatoRecentPaths(NagatoObject):

    def _set_max(self):
        yuki_data = "recent", "max"
        self._max = int(self._enquiry("YUKI.N > config", yuki_data))

    def _get_paths_exist(self, paths):
        for yuki_path in paths:
            if Path(yuki_path).exists():
                yield yuki_path

    def _sanitize(self, paths):
        yuki_paths = []
        for yuki_path in self._get_paths_exist(paths.split(",")):
            yuki_paths.append(yuki_path)
            if len(yuki_paths) >= self._max:
                break
        return yuki_paths

    def _get(self, default=None):
        yuki_paths = self._enquiry("YUKI.N > config", ("recent", "paths"))
        if yuki_paths == "":
            return default
        return self._sanitize(yuki_paths)

    def clear(self):
        self._raise("YUKI.N > config", ("recent", "paths", ""))

    def get_paths(self):
        return self._get()

    def set_path(self, path):
        yuki_paths = self._get([])
        if path in yuki_paths:
            yuki_paths.remove(path)
        yuki_paths.insert(0, path)
        yuki_data = "recent", "paths", ",".join(yuki_paths)
        self._raise("YUKI.N > config", yuki_data)

    def __init__(self, parent):
        self._parent = parent
        self._set_max()
