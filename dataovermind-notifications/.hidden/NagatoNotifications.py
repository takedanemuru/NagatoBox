#!/usr/bin/env python3

import gi.repository.GLib
import dbus
import dbus.service
import dbus.mainloop.glib
import subprocess

NOTIF_BUS_NAME    =  'org.freedesktop.Notifications'
NOTIF_OBJECT_PATH = '/org/freedesktop/Notifications'
NOTIF_INTERFACE   =  'org.freedesktop.Notifications'

class NotificationServer(dbus.service.Object):
    _id = 0
	
    @dbus.service.method(NOTIF_INTERFACE, in_signature='susssasa{sv}i', out_signature='u')
    def Notify(self, app_name, replace_id, app_icon, summary, body, actions, hints, expire_timeout):
        yuki_command = ["dataovermind-notifications","--notify"]
        if not replace_id:
            self._id += 1
            notification_id = self._id
        if summary : yuki_command.extend(["--summary",summary])
        if body : yuki_command.extend(["--body",body])
        subprocess.call(yuki_command)
        return notification_id

    @dbus.service.method(NOTIF_INTERFACE, in_signature='', out_signature='as')
    def GetCapabilities(self):
        return ("yuki.n > ...can you see this ? ", )

    @dbus.service.signal(NOTIF_INTERFACE, signature='uu')
    def NotificationClosed(self, id_in, reason_in):
        pass

    @dbus.service.method(NOTIF_INTERFACE, in_signature='u', out_signature='')
    def CloseNotification(self, id):
        pass

    @dbus.service.method(NOTIF_INTERFACE, in_signature='', out_signature='ssss')
    def GetServerInformation(self):
        return ('developping', 'http://takedanemuru.github.io', '42.5.14', '1.2') 

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    name = dbus.service.BusName(NOTIF_BUS_NAME, bus, do_not_queue=True) 
    NotificationServer(bus, NOTIF_OBJECT_PATH)
    mainloop = gi.repository.GLib.MainLoop()
    mainloop.run() # parsistent loop.
