
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Context import NagatoContextCore


class NagatoContextMenu(NagatoContextCore):

    def _initialize_children(self):
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")
