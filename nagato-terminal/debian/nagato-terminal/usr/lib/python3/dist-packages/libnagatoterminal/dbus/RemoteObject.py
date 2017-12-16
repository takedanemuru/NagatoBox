
from libnagatoterminal.dbus import Spec
from libnagatoterminal.dbus import Interface


class NagatoRemoteObject(object):

    def move_to_current_desktop(self):
        self._interface.MoveToCurrentDesktop()

    def __init__(self):
        self._interface = Interface.get_session(
            Spec.Service,
            Spec.ObjectPath,
            Spec.Interface
            )
