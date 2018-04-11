
import os
from pathlib import Path
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagato.util import FileManager
from libnagato.util import CssProvider
from libnagatotext.config.CssText import NagatoCssText


class NagatoCss(NagatoObject):

    def _ensure_paths(self):
        yuki_directory = GLib.get_user_config_dir()
        yuki_id = self._enquiry("YUKI.N > data", "id")
        self._directory = os.path.join(yuki_directory, yuki_id)
        self._directory_image = os.path.join(self._directory, "images")
        self._css = os.path.join(self._directory, "application.css")

    def _ensure_files(self):
        yuki_directory = self._enquiry("YUKI.N > resources", "images")
        for yuki_path in Path(yuki_directory).glob("*"):
            yuki_source = yuki_path.as_posix()
            yuki_target = os.path.join(self._directory_image, yuki_path.name)
            FileManager.ensure(yuki_source, yuki_target)

    def _reload(self):
        Path(self._css).write_text(self._css_text.get())
        CssProvider.set_to_application(self._css)

    def reload(self):
        self._reload()

    def __init__(self, parent):
        self._parent = parent
        self._css_text = NagatoCssText(self)
        self._ensure_paths()
        self._ensure_files()
        self._reload()
