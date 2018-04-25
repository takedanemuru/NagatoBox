
from pathlib import Path
from libnagato.menu.Sub import NagatoSubCore
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator


class NagatoRecentPaths(NagatoSubCore):

    def _on_map(self, widget):
        for yuki_child in self.get_children():
            self.remove(yuki_child)
        self._initialize_child_menus()
        self.show_all()

    def _set_recent_paths_menus(self, paths):
        NagatoItem(self, "Clear", "YUKI.N > clear recent paths")
        NagatoSeparator(self)
        for yuki_path in paths:
            yuki_title = Path(yuki_path).name
            NagatoItem(self, yuki_title, "YUKI.N > open file", yuki_path)

    def _initialize_child_menus(self):
        yuki_paths = self._enquiry("YUKI.N > recent paths")
        if yuki_paths is None:
            NagatoItem(self, "Not Found", "YUKI.N > NULL")
        else:
            self._set_recent_paths_menus(yuki_paths)

    def _set_variables(self):
        self._title = "Recent Files"
