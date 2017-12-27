
import os
import yaml
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import GdkPixbuf
from libnagato.util import CssProvider
from libnagatoterminal.util import FileManager


SETTINGS_PATH = ".config/NagatoBox/{}.config"


class NagatoResources(object):

    @classmethod
    def set_resources_directory(cls, path_to_humanoid_interface):
        yuki_path = os.path.dirname(path_to_humanoid_interface)
        NagatoResources._directory = yuki_path + "/resources"
        yuki_data_path = NagatoResources._directory+"/data.yaml"
        NagatoResources._data = yaml.load(open(yuki_data_path, "r"))

    def __getitem__(self, key):
        return NagatoResources._data[key]

    def _get_path_from_prefix(self, prefix):
        yuki_name = NagatoResources._data["name"] + prefix
        return NagatoResources._directory + "/" + yuki_name

    def set_css_to_application(self):
        CssProvider.set_to_application(self._get_path_from_prefix(".css"))

    def get_config_file(self):
        yuki_target_path = os.path.join(
            os.environ["HOME"],
            SETTINGS_PATH.format(NagatoResources._data["name"])
            )
        FileManager.ensure(
            self._get_path_from_prefix(".config"),
            yuki_target_path
            )
        return yuki_target_path

    def get_application_icon(self):
        yuki_path = self._get_path_from_prefix(".png")
        return GdkPixbuf.Pixbuf.new_from_file(yuki_path)
