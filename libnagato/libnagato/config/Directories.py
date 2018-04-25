
import os
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagato.util import FileManager


class NagatoDirectories(NagatoObject):

    def _get_target_path(self, name):
        yuki_id = self._enquiry("YUKI.N > data", "id")
        return os.path.join(GLib.get_user_config_dir(), yuki_id, name)

    def _ensure_file(self, name):
        yuki_source = self._enquiry("YUKI.N > resources", name)
        yuki_target = self._get_target_path(name)
        FileManager.ensure(yuki_source, yuki_target)
        return yuki_target

    def __init__(self, parent):
        self._parent = parent
        self._config_path = self._ensure_file("application.config")

    @property
    def config_path(self):
        return self._config_path
