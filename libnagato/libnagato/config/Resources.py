
import yaml
from pathlib import Path
from gi.repository.GdkPixbuf import Pixbuf
from libnagato.Object import NagatoObject


class NagatoResources(NagatoObject):

    def __getitem__(self, key):
        return self._data[key]

    def _get_path(self, name):
        yuki_directory = self._enquiry("YUKI.N > library directory")
        yuki_path = Path(yuki_directory).joinpath("resources", name)
        return yuki_path.as_posix()

    def get_pixbuf(self, name):
        yuki_path = self._get_path(name)
        return Pixbuf.new_from_file(yuki_path)

    def get_application_icon(self):
        return self.get_pixbuf("application.png")

    def get_absolute_path(self, name):
        return self._get_path(name)

    def __init__(self, parent):
        self._parent = parent
        yuki_path = Path(self._get_path("application.yaml"))
        self._data = yaml.load(yuki_path.open())
