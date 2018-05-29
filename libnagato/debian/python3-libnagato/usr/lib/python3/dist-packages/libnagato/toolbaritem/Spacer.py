
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoSpacer(NagatoObject):

    def _get_dummy_label(self):
        yuki_label = Gtk.Label(label="")
        yuki_label.set_hexpand(True)
        return yuki_label

    def __init__(self, parent):
        parent.pack_start(self._get_dummy_label(), False, True, 0)
