
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator
from libnagatowebbrowser.menu.action.GoBack import NagatoGoBack
from libnagatowebbrowser.menu.action.GoForward import NagatoGoForward
from libnagatowebbrowser.menu.action.StopLoading import NagatoStopLoading


class AsakuraNavigations(object):

    def __init__(self, parent):
        NagatoGoBack(parent)
        NagatoGoForward(parent)
        NagatoItem(parent, "Reload", "YUKI.N > reload")
        NagatoStopLoading(parent)     
        NagatoSeparator(parent)
