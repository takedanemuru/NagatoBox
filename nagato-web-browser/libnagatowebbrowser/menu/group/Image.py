
from libnagatowebbrowser.menu import action as MenuAction
from libnagatowebbrowser.menu.action.OpenImage import NagatoOpenImage
from libnagatowebbrowser.menu.action.SaveImage import NagatoSaveImage
from libnagatowebbrowser.menu.action.ImageSeparator import NagatoImageSeparator

class AsakuraImage(object):

    def __init__(self, parent):
        NagatoOpenImage(parent)
        NagatoSaveImage(parent)
        NagatoImageSeparator(parent)
