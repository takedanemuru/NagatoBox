
from libnagato.menu.Context import NagatoContextCore
from libnagatowebbrowser.menu.group.TabActions import AsakuraTabActions

class NagatoForTabLabel(NagatoContextCore):

    def _initialize_children(self):
        AsakuraTabActions(self)
