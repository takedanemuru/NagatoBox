
from libAPPNAME.Resources import NagatoResources
from libAPPNAME.MainWindow import NagatoMainWindow


class NagatoYuki(object):

    def N(self, message):
        NagatoMainWindow(self._resources)
        print("YUKI.N > また図書館に")

    def __init__(self):
        self._resources = NagatoResources()
