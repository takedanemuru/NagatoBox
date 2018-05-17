
from libnagatofontbook.Mikuru import Gi
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagatofontbook.Args import NagatoArgs
from libnagatofontbook.Application import NagatoApplication


class NagatoYuki(NagatoObject):

    def _inform_args(self, key):
        return self._args[key]

    def _inform_library_directory(self):
        return GLib.path_get_dirname(__file__)

    def N(self, message):
        if self._args["show-version"]:
            self._application.show_version()
        else:
            self._application.run()
            print("YUKI.N > また図書館に…")

    def __init__(self):
        Gi.require_version()
        self._parent = None
        self._args = NagatoArgs()
        self._application = NagatoApplication(self)
