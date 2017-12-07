
from libnagatoterminal import CssProvider
from libnagatoterminal.util.Args import NagatoArgs
from libnagatoterminal.Window import NagatoWindow
from libnagatoterminal.Unique import NagatoUnique
from libnagatoterminal.RemoteObject import NagatoRemoteObject


class NagatoYuki(object):

    def _start_application(self):
        yuki_unique = NagatoUnique()
        if yuki_unique.unique:
            CssProvider.set_to_application()
            NagatoWindow()
            print("YUKI.N > また図書館に…")
        else:
            yuki_remote_object = NagatoRemoteObject()
            yuki_remote_object.move_to_current_desktop()

    def N(self, message, user_data=None):
        if self._args.show_version:
            print("42.10.39")
        else:
            self._start_application()
            
    def __init__(self):
        self._args = NagatoArgs()
