
import os
import shutil
import configparser
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.util import Path

SETTINGS_PATH = ".config/NagatoBox/nagato-terminal.config"


class NagatoSettings(configparser.ConfigParser):

    def _save(self):
        yuki_target_path = os.path.join(Path.get_home(), SETTINGS_PATH)
        with open(yuki_target_path, 'w') as yuki_file:
            self.write(yuki_file)

    def save_window_rect(self, left, top, width, height):
        self["window"]["x"] = str(left)
        self["window"]["y"] = str(top)
        self["window"]["w"] = str(width)
        self["window"]["h"] = str(height)
        self._save()

    def load_window_rect(self):
        yuki_rect = NagatoRect(
            self.getint("window","x"),
            self.getint("window","y"),
            self.getint("window","w"),
            self.getint("window","h")
            )
        if 0 >= yuki_rect.width:
            return None
        else:
            return yuki_rect

    def __init__(self):
        configparser.ConfigParser.__init__(self)
        yuki_target_path = os.path.join(Path.get_home(), SETTINGS_PATH)
        if not os.path.exists(yuki_target_path):
            yuki_source_path = Path.get_resource("nagato-terminal.config")
            shutil.copy(yuki_source_path, yuki_target_path)
        self.read(yuki_target_path)
