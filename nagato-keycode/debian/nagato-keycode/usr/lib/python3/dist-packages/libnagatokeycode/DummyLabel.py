
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagato.util import CssProvider

TEMPLATE = "YUKI.N > key pressed \n\nGdk.keyval_name : {}\nkeyval : {}"


class NagatoDummyLabel(Gtk.Label,NagatoObject):

    def hello_world(self):
        yuki_real_name = GLib.get_real_name()
        self.set_text("YUKI.N > Welcome back, {}.".format(yuki_real_name))

    def say(self, something):
        self.set_text("YUKI.N > {} ?".format(something))

    def set_keyval(self, keyval):
        self.set_text(TEMPLATE.format(Gdk.keyval_name(keyval), keyval))

    def __init__(self, parent):
        self._parent = parent
        Gtk.Label.__init__(self)
        self.set_vexpand(True)
        self.set_hexpand(True)
        self.set_justify(Gtk.Justification.CENTER)
        self.set_text("YUKI.N > 見えてる？")
        CssProvider.set_to_widget(self, "dummy-label")
        self._parent.add(self)
