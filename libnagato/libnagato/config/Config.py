
import configparser
from pathlib import Path
from libnagato.Object import NagatoObject
from libnagato.config.Directories import NagatoDirectories
from libnagato.config.RecentPaths import NagatoRecentPaths


class NagatoConfig(configparser.ConfigParser, NagatoObject):

    def _save_config(self):
        yuki_path = Path(self._directories.config_path)
        with yuki_path.open(mode="w") as yuki_file:
            self.write(yuki_file)

    def _inform_config(self, user_data):
        yuki_group, yuki_key = user_data
        return self[yuki_group][yuki_key]

    def set_data2(self, group, key, value):
        self[group][key] = str(value)
        self._save_config()

    def clear_recent_paths(self):
        self._recent_paths.clear()

    def set_recent_path(self, path):
        self._recent_paths.set_path(path)

    def get_recent_paths(self):
        return self._recent_paths.get_paths()

    def __init__(self, parent):
        self._parent = parent
        configparser.ConfigParser.__init__(self)
        self._directories = NagatoDirectories(self)
        self.read(self._directories.config_path)
        self._recent_paths = NagatoRecentPaths(self)
