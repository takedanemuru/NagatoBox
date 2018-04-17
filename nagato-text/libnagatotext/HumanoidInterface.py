
from libnagatotext import GiVersion
from libnagato.Object import NagatoObject
from libnagatotext.Args import NagatoArgs
from libnagatotext.Application import NagatoApplication


class NagatoYuki(NagatoObject):

    def _inform_args(self, key):
        return self._args[key]

    def N(self, message):
        if self._args["show-version"]:
            self._application.show_version()
        else:
            self._application.run()
            print("YUKI.N > また図書館に…")

    def __init__(self):
        GiVersion.require()
        self._parent = None
        self._args = NagatoArgs()
        self._application = NagatoApplication(self)
