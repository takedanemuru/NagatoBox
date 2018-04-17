
import configparser
from pathlib import Path
from libnagato.Object import NagatoObject
from libnagatotext.config.Css import NagatoCss
from libnagatotext.config.Directories import NagatoDirectories


class NagatoConfig(configparser.ConfigParser, NagatoObject):

    def _save_config(self):
        yuki_path = Path(self._directories.config_path)
        with yuki_path.open(mode="w") as yuki_file:
            self.write(yuki_file)

    def _inform_config(self, user_data):
        yuki_group, yuki_key = user_data
        return self[yuki_group][yuki_key]

    def set_data(self, data):
        yuki_group, yuki_key, yuki_value = data
        self[yuki_group][yuki_key] = str(yuki_value)
        self._save_config()
        if yuki_group == "css":
            self._css.reload()

    def __init__(self, parent):
        self._parent = parent
        configparser.ConfigParser.__init__(self)
        self._directories = NagatoDirectories(self)
        self.read(self._directories.config_path)
        self._css = NagatoCss(self)
