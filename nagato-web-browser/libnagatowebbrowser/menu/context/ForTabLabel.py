
from libnagatowebbrowser.menu.context.ContextCore import NagatoContextCore
from libnagatowebbrowser.menu.group.TabActions import AsakuraTabActions

class NagatoForTabLabel(NagatoContextCore):

    def _initialize_children(self):
        AsakuraTabActions(self)
