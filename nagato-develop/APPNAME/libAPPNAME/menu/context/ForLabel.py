
from gi.repository import Gdk
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator
from libnagato.menu.Context import NagatoContextCore


class NagatoContextMenu(NagatoContextCore):

    def _initialize_children(self):
        NagatoItem(self, "Hello World.", "YUKI.N > hello world")
        NagatoSeparator(self)
        NagatoItem(self, "Alpha", "YUKI.N > alpha")
        NagatoItem(self, "Bravo", "YUKI.N > bravo")
        NagatoItem(self, "Charlie", "YUKI.N > charlie")
        NagatoItem(self, "Delta", "YUKI.N > delta")
