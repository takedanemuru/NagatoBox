
from dbus.mainloop.glib import DBusGMainLoop
from libnagatoterminal.dbus import Interface
from libnagatoterminal.dbus import Spec

class NagatoUnique(object):

    def _get_unique(self):
        for yuki_service in self._interface.ListNames():
            if yuki_service == self._service_name:
                return False
        return True

    def __init__(self):
        print("?")
        DBusGMainLoop(set_as_default=True)
        self._service_name = Spec.Servicetree
        self._interface = Interface.get_session(
            "org.freedesktop.DBus",
            "/",
            "org.freedesktop.DBus"
            )

    @property
    def unique(self):
        return self._get_unique()
