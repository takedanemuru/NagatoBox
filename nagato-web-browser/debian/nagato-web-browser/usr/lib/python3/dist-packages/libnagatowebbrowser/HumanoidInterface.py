
from libnagatowebbrowser.Resources import NagatoResources
from libnagatowebbrowser.MainWindow import NagatoMainWindow


class NagatoYuki(object):

    def N(self, message):
        self._resources.set_css_to_application()
        yuki_window = NagatoMainWindow()
        print("YUKI.N > また図書館に...")

    def __init__(self):
        self._resources = NagatoResources()
