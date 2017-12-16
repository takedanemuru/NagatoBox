
from libnagatoterminal.menu.item.sensitive.Copy import NagatoCopy
from libnagatoterminal.menu.item.sensitive.Paste import NagatoPaste


class AsakuraClipboard(object):

    def __init__(self, parent):
        NagatoCopy(parent)
        NagatoPaste(parent)
