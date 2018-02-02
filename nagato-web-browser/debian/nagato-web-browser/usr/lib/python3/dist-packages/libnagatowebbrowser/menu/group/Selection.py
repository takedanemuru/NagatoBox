
from libnagatowebbrowser.menu.action.SelectionCopy import NagatoSelectionCopy
from libnagatowebbrowser.menu.sub.SearchSelection import NagatoSearchSelection
from libnagatowebbrowser.menu.separator.Selection import NagatoSeparator

class AsakuraSelection(object):

    def __init__(self, parent):
        NagatoSelectionCopy(parent)
        NagatoSearchSelection(parent)
        NagatoSeparator(parent)
