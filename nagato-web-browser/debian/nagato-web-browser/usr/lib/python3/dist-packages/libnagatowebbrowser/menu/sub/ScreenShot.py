
from libnagato.menu.Item import NagatoItem
from libnagatowebbrowser.menu.sub.SubCore import NagatoSubCore


class NagatoScreenShot(NagatoSubCore):

    def _initialize_child_menus(self):
        # user_data are Webkit2.SnapshotRegion Enum
        NagatoItem(self, "Visible", "YUKI.N > snapshot", 0)
        NagatoItem(self, "Full Document", "YUKI.N > snapshot", 1)

    def _set_variables(self):
        self._title = "Snapshot"
        self._data_query = ""
