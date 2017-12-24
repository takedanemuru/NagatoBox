
from dbus.mainloop.glib import DBusGMainLoop
from libnagato.dbus import Interface


class NagatoUnique(object):

    def _get_unique(self):
        for yuki_service in self._interface.ListNames():
            if yuki_service == self._service_name:
                return False
        return True

    def __init__(self, service_name):
        DBusGMainLoop(set_as_default=True)
        self._service_name = service_name
        self._interface = Interface.get_session(
            "org.freedesktop.DBus",
            "/",
            "org.freedesktop.DBus"
            )

    @property
    def is_unique(self):
        return self._get_unique()
