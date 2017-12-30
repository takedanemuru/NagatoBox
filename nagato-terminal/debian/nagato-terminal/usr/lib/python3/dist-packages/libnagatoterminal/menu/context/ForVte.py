
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator
from libnagatoterminal.menu.context.ContextCore import NagatoContextCore
from libnagatoterminal.menu.group.Clipboard import AsakuraClipboard
from libnagatoterminal.menu.group.GridActions import AsakuraGridActions
from libnagatoterminal.menu.item.action.AddNewTab import NagatoAddNewTab


class NagatoForVte(NagatoContextCore):

    def _on_middle_click(self, user_data=None):
        self._raise("YUKI.N > paste")

    def _initialize_children(self):
        AsakuraClipboard(self)
        NagatoSeparator(self)
        AsakuraGridActions(self)
        NagatoSeparator(self)
        NagatoAddNewTab(self)
        NagatoItem(self, "Close Current VTE", "YUKI.N > destroy")
        NagatoSeparator(self)
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")
