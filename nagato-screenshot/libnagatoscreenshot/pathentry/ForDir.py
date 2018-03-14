
from gi.repository import GLib
from libnagatoscreenshot.pathentry.PathEntry import NagatoPathEntry as TFEI


class NagatoPathEntry(TFEI):

    def _get_message(self):
        return "YUKI.N > dir name changed"

    def _on_map(self, *args):
        self._entry.set_text(GLib.get_home_dir())
        self._entry.set_editable(False)

    def _get_label(self):
        return "Directory : "
