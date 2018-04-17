
from pathlib import Path
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Sub import NagatoSubCore
from gi.repository import GLib

PATH = "/gtksourceview-3.0/styles"


class NagatoSchems(NagatoSubCore):

    def _add_schemes(self, directory):
        yuki_path = Path(directory)
        if not yuki_path.exists():
            return
        for yuki_scheme in sorted(yuki_path.glob("*.xml")):
            yuki_name = yuki_scheme.stem
            NagatoItem(self, yuki_name, "YUKI.N > scheme", yuki_name)

    def _initialize_child_menus(self):
        for yuki_directory in GLib.get_system_data_dirs():
            self._add_schemes(yuki_directory + PATH)
        self._add_schemes(GLib.get_user_data_dir() + PATH)

    def _set_variables(self):
        self._title = "Style Schemes"
