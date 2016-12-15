#!/usr/bin/env python3

# (c) takeda.nemuru <takeda.nemuru@yandex.com> 2016-
# This script is licensed under S.O.S. License

import subprocess
import dbus
import dbus.service as Service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

DBusService = "org.freedesktop.Notifications"
DBusObjectPath = "/org/freedesktop/Notifications"
DBusInterface = "org.freedesktop.Notifications"


class YukiNotifications(Service.Object):
    _persistent_id = 1000

    def __init__(self):
        pass

    def N(self, message):
        DBusGMainLoop(set_as_default=True)
        yuki_name = Service.BusName(DBusService, dbus.SessionBus())
        Service.Object.__init__(self, yuki_name, DBusObjectPath)
        self._persistent_loop = GLib.MainLoop()
        self._persistent_loop.run()

    @Service.method(DBusInterface, in_signature="susssasa{sv}i", out_signature="u")
    def Notify(self, app_name, replaces_id, app_icon, summary, body,actions, hints, expire_timeout):
        yuki_command = ["nagato-notifications","--notify"]
        if app_name: yuki_command.extend(["--app", app_name])
        # NOTE : replaces_id == 0 means `do not replace id`
        #        see https://developer.gnome.org/notification-spec/ for more detail.
        if replaces_id == 0: self._persistent_id += 1
        yuki_id = self._persistent_id if replaces_id == 0 else replaces_id
        if summary: yuki_command.extend(["--summary", summary])
        if body: yuki_command.extend(["--body", body])
        for yuki_action in actions:
            pass
        for yuki_key, yuki_value in hints.items():
            if yuki_key == "urgency": yuki_command.extend(["--urgency", str(int(yuki_value))])
            # if yuki_key == "category": yuki_command.extend(["--category",str(yuki_value)]
        subprocess.call(yuki_command)

        return yuki_id

    @Service.method(DBusInterface, in_signature="", out_signature="as")
    def GetCapabilities(self):
        return (["body", "body-markup", "persistence"])

    @Service.method(DBusInterface, in_signature="u", out_signature="")
    def CloseNotification(self, id):
        yuki_command = ["nagato-notifications", "--close", id]
        subprocess.call(yuki_command)
        self.NotificationClosed(id, 3)

    @Service.method(DBusInterface, in_signature="", out_signature="ssss")
    def GetServerInformation(self):
        return ("nagato-notifications", "https://takedanemuru.github.io", "42.5.31", "1.2")

    @Service.signal(DBusInterface, signature="uu")
    def NotificationClosed(self, id, reason):
        # NOTE : reason MUST be 1, 2, 3 or 4. See below.
        if reason == 1: print("Notification id:", id, "expired.")
        if reason == 2: print("Notification id:", id, "was dismissed by the user.")
        if reason == 3: print("Notification id:", id, "was closed by a call to CloseNotification.")
        if reason == 4: print("Notification id:", id, "was closed by undefined/reserved reasons.")

    @Service.signal(DBusInterface, signature="us")
    def ActionInvoked(self, id, action):
        # Who cares ?
        pass

if __name__ == "__main__":
    YUKI = YukiNotifications()
    YUKI.N("> Ready ?")