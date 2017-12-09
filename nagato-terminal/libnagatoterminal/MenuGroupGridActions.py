
from libnagatoterminal.SubMenuVteNew import NagatoSubMenuVteNew
from libnagatoterminal.SubMenuVteExpand import NagatoSubMenuVteExpand
from libnagatoterminal.SubMenuVteShrink import NagatoSubMenuVteShrink


class AsakuraMenuGroupGridActions(object):

    def __init__(self, parent):
        NagatoSubMenuVteNew(parent)
        NagatoSubMenuVteExpand(parent)
        NagatoSubMenuVteShrink(parent)
