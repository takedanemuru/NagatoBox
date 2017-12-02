
from libnagatoterminal import CssProvider
from libnagatoterminal.util.Args import NagatoArgs
from libnagatoterminal.Window import NagatoWindow
from libnagatoterminal.DBusServiceObject import NagatoDBusServiceObject


class NagatoYuki(object):

    def _start_application(self):
        yuki_dbus = NagatoDBusServiceObject()
        if yuki_dbus.unique:
            CssProvider.set_to_application()
            NagatoWindow()
        else:
            print("YUKI.N > nagato-terminal has been activated.")

    def N(self, message, user_data=None):
        if self._args.show_version:
            print("42.10.38")
        else:
            self._start_application()
            
    def __init__(self):
        self._args = NagatoArgs()
