
from libnagatoterminal.menu.context.ContextCore import NagatoContextCore
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator
from libnagatoterminal.menu.item.action.AddNewTab import NagatoAddNewTab


class NagatoContextMenu(NagatoContextCore):

    def _on_middle_click(self, user_data=None):
        self._raise("YUKI.N > destroy")

    def _initialize_children(self):
        NagatoItem(self, "Set Tab Title", "YUKI.N > set tab title")
        NagatoSeparator(self)
        NagatoAddNewTab(self)
        NagatoItem(self, "Close Current VTE", "YUKI.N > destroy")
