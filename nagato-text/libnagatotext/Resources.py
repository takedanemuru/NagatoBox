
import os
import yaml
from pathlib import Path
from gi.repository import GLib
from gi.repository import GdkPixbuf


class NagatoResources(object):

    def __getitem__(self, key):
        return self._data[key]

    def _get_path(self, name):
        yuki_directory = GLib.path_get_dirname(__file__)
        return os.path.join(yuki_directory, "resources", name)

    def get_pixbuf(self, name):
        yuki_path = self._get_path(name)
        return GdkPixbuf.Pixbuf.new_from_file(yuki_path)

    def get_application_icon(self):
        return self.get_pixbuf("application.png")

    def get_absolute_path(self, name):
        return self._get_path(name)

    def __init__(self):
        yuki_path = Path(self._get_path("application.yaml"))
        self._data = yaml.load(yuki_path.open())
