
from libnagatodevelop import GiRequireVersion
from libnagatodevelop import Find
from libnagatodevelop.Args import NagatoArgs
from libnagatodevelop.Resources import NagatoResources
from libnagatodevelop.MainWindow import NagatoMainWindow


class NagatoYuki(object):

    def N(self, message):
        if self._args["show-version"]:
            print(self._resources["version"])
        elif self._args["lines-of-code"]:
            Find.lines_of_code()
        elif self._args["find"] is not None:
            Find.find(self._args["find"])
        else:
            self._resources.set_css_to_application()
            NagatoMainWindow(self._args, self._resources)
            print("YUKI.N > また図書館に…")

    def __init__(self):
        self._args = NagatoArgs()
        self._resources = NagatoResources()
