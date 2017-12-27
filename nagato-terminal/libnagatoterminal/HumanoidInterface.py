
from libnagato.dbus.Unique import NagatoUnique
from libnagatoterminal.util.Args import NagatoArgs
from libnagatoterminal.Window import NagatoWindow
from libnagatoterminal.dbus.RemoteObject import NagatoRemoteObject
from libnagatoterminal.Resources import NagatoResources


class NagatoYuki(object):

    def _start_application(self):
        yuki_unique = NagatoUnique(self._resources["id"])
        if yuki_unique.is_unique:
            self._resources.set_css_to_application()
            NagatoWindow()
            print("YUKI.N > また図書館に…")
        else:
            yuki_remote_object = NagatoRemoteObject()
            yuki_remote_object.move_to_current_desktop()

    def N(self, message, user_data=None):
        if self._args.show_version:
            print(self._resources["version"])
        else:
            self._start_application()

    def __init__(self):
        self._args = NagatoArgs()
        NagatoResources.set_resources_directory(__file__)
        self._resources = NagatoResources()
