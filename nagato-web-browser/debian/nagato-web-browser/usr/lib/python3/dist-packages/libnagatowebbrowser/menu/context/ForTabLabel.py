
from libnagato.menu.Context import NagatoContextCore
from libnagatowebbrowser.menu.group.TabActions import AsakuraTabActions

class NagatoContextMenu(NagatoContextCore):

    def _on_middle_click(self, user_data=None):
        self._raise("YUKI.N > close current tab")

    def _initialize_children(self):
        AsakuraTabActions(self)
