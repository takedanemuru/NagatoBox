
import os
import shutil
import configparser
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.Resources import NagatoResources


class NagatoSettings(configparser.ConfigParser):

    def _save(self):
        yuki_target_path = os.path.join(self._resources.get_config_file())
        with open(yuki_target_path, "w") as yuki_file:
            self.write(yuki_file)

    def save_window_rect(self, left, top, width, height):
        self["window"]["x"] = str(left)
        self["window"]["y"] = str(top)
        self["window"]["w"] = str(width)
        self["window"]["h"] = str(height)
        self._save()

    def load_window_rect(self):
        yuki_rect = NagatoRect(
            self.getint("window", "x"),
            self.getint("window", "y"),
            self.getint("window", "w"),
            self.getint("window", "h")
            )
        return None if 0 >= yuki_rect.width else yuki_rect

    def __init__(self):
        configparser.ConfigParser.__init__(self)
        self._resources = NagatoResources()
        self.read(self._resources.get_config_file())
