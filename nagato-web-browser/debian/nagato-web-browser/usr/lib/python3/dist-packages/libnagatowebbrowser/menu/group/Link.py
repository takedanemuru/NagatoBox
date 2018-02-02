
from libnagatowebbrowser.menu.action.LinkOpen import NagatoLinkOpen
from libnagatowebbrowser.menu.action.LinkSave import NagatoLinkSave
from libnagatowebbrowser.menu.separator.Link import NagatoSeparator


class AsakuraLink(object):

    def __init__(self, parent):
        NagatoLinkOpen(parent)
        NagatoLinkSave(parent)
        NagatoSeparator(parent)
