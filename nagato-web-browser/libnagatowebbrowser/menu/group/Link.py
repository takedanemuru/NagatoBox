
from libnagatowebbrowser.menu.action.LinkOpen import NagatoLinkOpen
from libnagatowebbrowser.menu.action.LinkSave import NagatoLinkSave
from libnagatowebbrowser.menu.action.LinkSeparator import NagatoLinkSeparator


class AsakuraLink(object):

    def __init__(self, parent):
        NagatoLinkOpen(parent)
        NagatoLinkSave(parent)
        NagatoLinkSeparator(parent)
