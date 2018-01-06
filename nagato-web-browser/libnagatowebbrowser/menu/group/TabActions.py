
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator
from libnagatowebbrowser.menu.action.CloseTab import NagatoCloseTab


class AsakuraTabActions(object):

    def __init__(self, parent):
        NagatoItem(parent, "New Tab", "YUKI.N > add new tab")
        NagatoCloseTab(parent)
