
import os
import yaml
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import GdkPixbuf
from libnagato.util import CssProvider
from libnagato.util import FileManager

CONFIG_PATH = ".config/NagatoBox/{}.config"


class NagatoResources(object):

    def __getitem__(self, key):
        return self._data[key]

    def _get_path_from_prefix(self, prefix):
        return os.path.join(self._directory, ("application" + prefix))

    def _get_target_path_for_config_file(self):
        yuki_config_path = CONFIG_PATH.format(self._data["name"])
        return os.path.join(os.environ["HOME"], yuki_config_path)

    def get_image_path(self, file_name):
        return os.path.join(self._directory, "images", file_name)

    def get_config_file(self):
        yuki_source_path = self._get_path_from_prefix(".config")
        yuki_target_path = self._get_target_path_for_config_file()
        FileManager.ensure(yuki_source_path, yuki_target_path)
        return yuki_target_path

    def get_application_icon(self):
        yuki_path = self._get_path_from_prefix(".png")
        return GdkPixbuf.Pixbuf.new_from_file(yuki_path)

    def set_css_to_application(self):
        CssProvider.set_to_application(self._get_path_from_prefix(".css"))

    def __init__(self):
        self._directory = os.path.join(os.path.dirname(__file__), "resources")
        self._data = yaml.load(open(self._get_path_from_prefix(".yaml"), "r"))
