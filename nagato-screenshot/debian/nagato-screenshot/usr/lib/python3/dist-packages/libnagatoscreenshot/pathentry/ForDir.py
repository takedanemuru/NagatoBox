
from gi.repository import GLib
from libnagatoscreenshot.pathentry.PathEntry import NagatoPathEntry as TFEI
from libnagatoscreenshot.dialog.DirectoryChooser import NagatoDirectoryChooser


class NagatoPathEntry(TFEI):

    def _set_directory(self):
        yuki_config = self._enquiry("YUKI.N > config")
        self._directory = yuki_config.get_config("files", "last_directory")
        if self._directory == "":
            self._directory = GLib.get_home_dir()

    def _on_icon_pressed(self, entry, position, event):
        if position != 1:
            return
        yuki_path = NagatoDirectoryChooser.call(self._directory)
        print(yuki_path)
        if yuki_path is None:
            return
        self._entry.set_text(yuki_path.replace(GLib.get_home_dir(), "~"))
        yuki_config = self._enquiry("YUKI.N > config")
        yuki_config.set_config("files", "last_directory", yuki_path)
        self._raise("YUKI.N > dir name changed", yuki_path)

    def _get_message(self):
        return "YUKI.N > dir name changed"

    def _on_map(self, *args):
        self._set_directory()
        self._entry.set_text(self._directory.replace(GLib.get_home_dir(), "~"))
        self._entry.set_editable(False)
        self._entry.set_icon_from_icon_name(1, "folder")
        self._entry.set_icon_tooltip_text(1, "click to change directory")
        self._entry.connect("icon-press", self._on_icon_pressed)

    def _get_label(self):
        return "Directory : "
