
from dbus.mainloop.glib import DBusGMainLoop
from libnagatoterminal.dbus import Spec
from libnagatoterminal.dbus import Interface


class NagatoUnique(object):

    def _get_unique(self):
        for yuki_service in self._interface.ListNames():
            if yuki_service == Spec.Service:
                return False
        return True

    def __init__(self):
        DBusGMainLoop(set_as_default=True)
        self._interface = Interface.get_session(
            "org.freedesktop.DBus",
            "/",
            "org.freedesktop.DBus"
            )

    @property
    def unique(self):
        return self._get_unique()
