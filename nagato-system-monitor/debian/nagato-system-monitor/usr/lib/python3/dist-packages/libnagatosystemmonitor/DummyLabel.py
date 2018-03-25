
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.util import CssProvider


class NagatoDummyLabel(Gtk.Label,NagatoObject):

    def queue(self, user_data):
        yuki_text = "CPU: {:.2%}\t".format(user_data["cpu"])
        yuki_text += "Memory: {:.2%}\t".format(user_data["memory"])
        yuki_text += "Swap: {:.2%}\t".format(user_data["swap"])
        yuki_text += "Processes: {} ".format(user_data["count"])
        self.set_text(yuki_text)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Label.__init__(self)
        #self.set_vexpand(True)
        #self.set_hexpand(True)
        self.set_padding(8, 8)
        self.set_text("YUKI.N > 見えてる？")
        CssProvider.set_to_widget(self, "dummy-label")
