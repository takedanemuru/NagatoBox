
import dbus
import dbus.service as Service
from dbus.mainloop.glib import DBusGMainLoop
from libnagato.Object import NagatoObject
from libnagatoterminal.dbus import Spec

Property = dbus.PROPERTIES_IFACE


class NagatoServiceObject(Service.Object, NagatoObject):

    def __init__(self, parent):
        self._parent = parent
        DBusGMainLoop(set_as_default=True)
        yuki_name = Service.BusName(Spec.Service, dbus.SessionBus())
        Service.Object.__init__(self, yuki_name, Spec.ObjectPath)

    @Service.method(Spec.Interface, in_signature="", out_signature="")
    def MoveToCurrentDesktop(self):
        self._raise("YUKI.N > move to current desktop")

    @Service.method(Property, in_signature='ss', out_signature='v')
    def Get(self, interface_name, property_name):
        return self.GetAll(interface_name)[property_name]

    @Service.method(Property, in_signature='ssv')
    def Set(self, interface_name, property_name, value):
        if interface_name == Spec.Interface:
            print("You can't change any property.")

    @Service.method(Property, in_signature='s', out_signature='a{sv}')
    def GetAll(self, interface_name):
        if interface_name == Spec.Interface:
            return {"Ready": True, "Hello": "Hello"}
        else:
            return None

    @Service.signal(Property, signature="sa{sv}as")
    def PropertyChanged(
            self,
            interface_name,
            changed_properties,
            indicated_properties
            ):
        print("properties changed.")
