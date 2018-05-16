
from libnagatodevelop.Mikuru import Gi
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagatodevelop import Find
from libnagatodevelop.Args import NagatoArgs
from libnagatodevelop.Application import NagatoApplication

class NagatoYuki(NagatoObject):

    def _inform_args(self, key):
        return self._args[key]

    def _inform_library_directory(self):
        return GLib.path_get_dirname(__file__)

    def N(self, message):
        if self._args["show-version"]:
            self._application.show_version()
        elif self._args["lines-of-code"]:
            Find.lines_of_code()
        elif self._args["find"] is not None:
            Find.find(self._args["find"])
        else:
            self._application.run()
            print("YUKI.N > また図書館に…")

    def __init__(self):
        self._parent = None
        Gi.require_version()
        self._args = NagatoArgs()
        self._application = NagatoApplication(self)
