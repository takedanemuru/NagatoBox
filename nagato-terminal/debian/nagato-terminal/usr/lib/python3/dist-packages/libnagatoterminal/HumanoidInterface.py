
from libnagatoterminal import GiVersion
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagatoterminal.util.Args import NagatoArgs
from libnagatoterminal.Application import NagatoApplication


class NagatoYuki(NagatoObject):

    def _inform_args(self, key):
        return self._args[key]

    def _inform_library_directory(self):
        return GLib.path_get_dirname(__file__)

    def N(self, message):
        if self._args["show-version"]:
            print(self._resources["version"])
        else:
            self._application.run()
            print("YUKI.N > また図書館に…")
        """
        else:
            yuki_remote_object = NagatoRemoteObject()
            yuki_remote_object.move_to_current_desktop()
        """

    def __init__(self):
        GiVersion.require()
        self._args = NagatoArgs()
        # self._unique = NagatoUnique(self._resources["id"])
        self._application = NagatoApplication(self)
