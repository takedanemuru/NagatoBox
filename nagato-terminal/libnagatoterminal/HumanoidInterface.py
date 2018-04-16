
from libnagatoterminal import GiVersion
from libnagato.dbus.Unique import NagatoUnique
from libnagatoterminal.util.Args import NagatoArgs
from libnagatoterminal.Window import NagatoWindow
from libnagatoterminal.dbus.RemoteObject import NagatoRemoteObject
from libnagatoterminal.Resources import NagatoResources


class NagatoYuki(object):

    def N(self, message):
        if self._args["show-version"]:
            print(self._resources["version"])
        elif self._unique.is_unique:
            self._resources.set_css_to_application()
            NagatoWindow()
            print("YUKI.N > また図書館に…")
        else:
            yuki_remote_object = NagatoRemoteObject()
            yuki_remote_object.move_to_current_desktop()

    def __init__(self):
        GiVersion.require()
        self._args = NagatoArgs()
        self._resources = NagatoResources()
        self._unique = NagatoUnique(self._resources["id"])
