
from libnagatoterminal.menu.Item import NagatoItem
from libnagatoterminal.menu.context.ContextCore import NagatoContextCore

class NagatoForChrome(NagatoContextCore):

    def _initialize_children(self):
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")
