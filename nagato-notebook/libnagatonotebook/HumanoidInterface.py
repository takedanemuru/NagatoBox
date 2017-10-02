
from libnagatonotebook.Window import NagatoWindow
from libnagatonotebook import CssProvider


class NagatoYuki(object):

    def N(self, message):
        CssProvider.set_to_application()
        NagatoWindow()

    def __init__(self):
        pass
