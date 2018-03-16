
import time
from libnagatoscreenshot.Args import NagatoArgs
from libnagatoscreenshot.Resources import NagatoResources
from libnagatoscreenshot.Screenshot import NagatoScreenshot


class NagatoYuki(object):

    def N(self, message):
        if self._args["show-version"]:
            print(self._resources["version"])
        else:
            time.sleep(self._args["delay"])
            self._resources.set_css_to_application()
            NagatoScreenshot(self._args, self._resources)
            print("YUKI.N > また図書館に…")

    def __init__(self):
        self._args = NagatoArgs()
        self._resources = NagatoResources()
