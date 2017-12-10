
from libnagatoterminal.SubMenuNew import NagatoSubMenuNew
from libnagatoterminal.SubMenuExpand import NagatoSubMenuExpand
from libnagatoterminal.SubMenuShrink import NagatoSubMenuShrink


class AsakuraGridActions(object):

    def __init__(self, parent):
        NagatoSubMenuNew(parent)
        NagatoSubMenuExpand(parent)
        NagatoSubMenuShrink(parent)
