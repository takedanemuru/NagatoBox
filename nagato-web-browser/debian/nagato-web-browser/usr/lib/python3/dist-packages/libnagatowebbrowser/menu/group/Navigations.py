
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator
from libnagatowebbrowser.menu.action.GoBack import NagatoGoBack
from libnagatowebbrowser.menu.action.GoForward import NagatoGoForward
from libnagatowebbrowser.menu.action.StopLoading import NagatoStopLoading
from libnagatowebbrowser.menu.action.EnableJavascript import NagatoEnableJavascript


class AsakuraNavigations(object):

    def __init__(self, parent):
        NagatoItem(parent, "URL", "YUKI.N > dialog url")
        NagatoGoBack(parent)
        NagatoGoForward(parent)
        NagatoItem(parent, "Reload", "YUKI.N > reload")
        NagatoStopLoading(parent)
        NagatoEnableJavascript(parent)
        NagatoSeparator(parent)
