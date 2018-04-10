
import os
from pathlib import Path
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagato.util import FileManager
from libnagato.util import CssProvider


class NagatoCss(NagatoObject):

    def _ensure_paths(self):
        yuki_directory = GLib.get_user_config_dir()
        yuki_id = self._enquiry("YUKI.N > data", "id")
        self._directory = os.path.join(yuki_directory, yuki_id)
        self._directory_image = os.path.join(self._directory, "images")
        self._css = os.path.join(self._directory, "application.css")

    def _get_css_text(self):
        yuki_source = self._enquiry("YUKI.N > resources", "application.css")
        yuki_text = Path(yuki_source).read_text()
        return yuki_text

    def _ensure_css(self):
        yuki_text = self._get_css_text()
        Path(self._css).write_text(yuki_text)

    def _ensure_files(self):
        yuki_directory = self._enquiry("YUKI.N > resources", "images")
        for yuki_path in Path(yuki_directory).glob("*"):
            yuki_source = yuki_path.as_posix()
            yuki_target = os.path.join(self._directory_image, yuki_path.name)
            FileManager.ensure(yuki_source, yuki_target)

    def set_css_to_application(self):
        CssProvider.set_to_application(self._css)

    def __init__(self, parent):
        self._parent = parent
        self._ensure_path()
        self._ensure_files()
        self._ensure_css()
