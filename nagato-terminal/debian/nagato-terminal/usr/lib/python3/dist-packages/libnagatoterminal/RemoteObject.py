
import dbus

DBusService = "box.nagato.terminal"
DBusObjectPath = "/box/nagato/terminal"
DBusInterface = "box.nagato.terminal"


class NagatoRemoteObject(object):

    def move_to_current_desktop(self):
        self._interface.MoveToCurrentDesktop()

    def __init__(self):
        yuki_bus = dbus.SessionBus()
        yuki_object = yuki_bus.get_object(DBusService, DBusObjectPath)
        self._interface = dbus.Interface(yuki_object, DBusInterface)
