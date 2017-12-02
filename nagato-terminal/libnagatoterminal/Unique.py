
import dbus

DBusService = "box.nagato.terminal"


class NagatoUnique(object):

    def __init__(self):
        self._unique = True
        yuki_bus = dbus.SessionBus()
        yuki_proxy = yuki_bus.get_object("org.freedesktop.DBus","/")
        yuki_interface = dbus.Interface(yuki_proxy, "org.freedesktop.DBus")
        for yuki_service in yuki_interface.ListNames():
            if yuki_service == DBusService:
                self._unique = False
                break

    @property
    def unique(self):
        return self._unique
