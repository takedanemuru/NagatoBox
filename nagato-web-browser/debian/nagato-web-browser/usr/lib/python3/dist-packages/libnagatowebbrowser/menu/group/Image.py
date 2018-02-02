
from libnagatowebbrowser.menu.action.OpenImage import NagatoOpenImage
from libnagatowebbrowser.menu.action.SaveImage import NagatoSaveImage
from libnagatowebbrowser.menu.separator.Image import NagatoSeparator

class AsakuraImage(object):

    def __init__(self, parent):
        NagatoOpenImage(parent)
        NagatoSaveImage(parent)
        NagatoSeparator(parent)
