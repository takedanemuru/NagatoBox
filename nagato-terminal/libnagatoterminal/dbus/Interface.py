
import dbus


def get_session(service, object_path, interface):
    yuki_bus = dbus.SessionBus()
    yuki_object = yuki_bus.get_object(service, object_path)
    return dbus.Interface(yuki_object, interface)
