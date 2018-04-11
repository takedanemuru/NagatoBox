
import configparser
from pathlib import Path
from libnagato.Object import NagatoObject
from libnagatotext.config.Window import NagatoWindow
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

    def _yuki_n_config_changed(self):
        self._save_config()

    def set_data(self, data):
        yuki_group, yuki_key, yuki_value = data
        self[yuki_group][yuki_key] = str(yuki_value)
        self._save_config()
        if yuki_group == "css":
            self._css.reload()

    def save_window_position(self, gtk_window):
        self._window_config.save_window_position(gtk_window)

    def setup_window(self, gtk_window):
        gtk_window.set_default_size(800, 640)
        self._window_config.load_window_position(gtk_window)
        yuki_icon_pixbuf = self._enquiry("YUKI.N > pixbuf", "application.png")
        gtk_window.set_icon(yuki_icon_pixbuf)

    def __init__(self, parent):
        self._parent = parent
        configparser.ConfigParser.__init__(self)
        self._directories = NagatoDirectories(self)
        self.read(self._directories.config_path)
        self._window_config = NagatoWindow(self)
        self._css = NagatoCss(self)
