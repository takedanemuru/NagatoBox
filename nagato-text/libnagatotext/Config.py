
import configparser
from gi.repository import Gtk
from pathlib import Path


class NagatoConfig(configparser.ConfigParser):

    def _save(self):
        yuki_path = Path(self._path_to_config)
        with yuki_path.open(mode="w") as yuki_file:
            self.write(yuki_file)

    def save_window_position(self, gtk_window):
        yuki_left, yuki_top = gtk_window.get_position()
        yuki_width, yuki_height = gtk_window.get_size()
        self["window"]["x"] = str(yuki_left)
        self["window"]["y"] = str(yuki_top)
        self["window"]["w"] = str(yuki_width)
        self["window"]["h"] = str(yuki_height)
        self._save()

    def load_window_position(self, gtk_window):
        yuki_left = self.getint("window", "x")
        yuki_top = self.getint("window", "y")
        yuki_width = self.getint("window", "w")
        yuki_height = self.getint("window", "h")
        if 0 >= yuki_width:
            gtk_window.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        else:
            gtk_window.move(yuki_left, yuki_top)
            gtk_window.set_default_size(yuki_width, yuki_height)

    def __init__(self, path_to_config):
        configparser.ConfigParser.__init__(self)
        self._path_to_config = path_to_config
        self.read(self._path_to_config)
