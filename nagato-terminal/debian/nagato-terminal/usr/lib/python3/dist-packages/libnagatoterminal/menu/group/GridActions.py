
from libnagatoterminal.menu.sub.gridactions.New import NagatoNew
from libnagatoterminal.menu.sub.gridactions.Expand import NagatoExpand
from libnagatoterminal.menu.sub.gridactions.Shrink import NagatoShrink


class AsakuraGridActions(object):

    def __init__(self, parent):
        NagatoNew(parent)
        NagatoExpand(parent)
        NagatoShrink(parent)
