#!/usr/bin/env python3

# (c) takeda.nemuru <takeda.nemuru@yandex.com> 2016-
# this script is licensed under S.O.S. License

import subprocess
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

DBusService = "org.freedesktop.Notifications"
DBusObjectPath = "/org/freedesktop/Notifications"
DBusInterface = "org.freedesktop.Notifications"

class NotificationServer(dbus.service.Object):
    _id = 0
	
    @dbus.service.method(DBusInterface, in_signature='susssasa{sv}i', out_signature='u')
    def Notify(self, app_name, replace_id, app_icon, summary, body, actions, hints, expire_timeout):
        yuki_command = ["dataovermind-notifications","--notify"]
        if app_name: yuki_command.extend(["--app", app_name])
        if not replace_id: self._id += 1
        yuki_id = replace_id if replace_id else self._id
        #yuki_command.extend(["--id", str(yuki_id)])
        if summary: yuki_command.extend(["--summary", summary])
        if body: yuki_command.extend(["--body", body])
        for yuki_key, yuki_value in hints.items():
            if yuki_key == "urgency": yuki_command.extend(["--urgency", str(int(yuki_value))])
        #if expire_timeout: yuki_command.extend(["--timeout", str(expire_timeout)])
        subprocess.call(yuki_command)
        return yuki_id

    @dbus.service.method(DBusInterface, in_signature='', out_signature='as')
    def GetCapabilities(self):
        return (["body", "persistence"])

    @dbus.service.signal(DBusInterface, signature='uu')
    def NotificationClosed(self, id_in, reason_in):
        #Gambas3's dbus implementation cannot raise signal...
        pass

    @dbus.service.method(DBusInterface, in_signature='u', out_signature='')
    def CloseNotification(self, id):
        yuki_command = ["dataovermind-notifications", "--close"]
        subprocess.call(yuki_command)

    @dbus.service.method(DBusInterface, in_signature='', out_signature='ssss')
    def GetServerInformation(self):
        return ("do not try it yourself", "https://takedanemuru.github.io", "42.5.24", "1.2") 

if __name__ == '__main__':
    DBusGMainLoop(set_as_default=True)
    nagato_service = dbus.service.BusName(DBusService, dbus.SessionBus(), do_not_queue=True) 
    nagato_server = NotificationServer(dbus.SessionBus(), DBusObjectPath)
    nagato_loop = GLib.MainLoop()
    nagato_loop.run() # parsistent loop

