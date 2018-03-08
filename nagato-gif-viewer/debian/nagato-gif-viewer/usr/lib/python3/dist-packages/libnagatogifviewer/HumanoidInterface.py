
from libnagatogifviewer.Args import NagatoArgs
from libnagatogifviewer.Resources import NagatoResources
from libnagatogifviewer.MainWindow import NagatoMainWindow


class NagatoYuki(object):

    def N(self, message):
        if self._args["show-version"]:
            print(self._resources["version"])
        else:
            self._resources.set_css_to_application()
            NagatoMainWindow(self._args, self._resources)
            print("YUKI.N > また図書館に…")

    def __init__(self):
        self._args = NagatoArgs()
        self._resources = NagatoResources()
