
from gi.repository import Gtk
from libnagato.util import CssProvider


TEMPLATE = \
    "<span size='large'><u>YOUR CHANGES ARE NOT SAVED !!</u></span>\n"\
    "\n"\
    "If you select Discard,\n"\
    "All your changes will be lost.\n"


class NagatoDialogLabel(Gtk.Label):

    def __init__(self, content_area):
        Gtk.Label.__init__(self)
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.set_markup(TEMPLATE)
        self.set_padding(8, 8)
        CssProvider.set_to_widget(self, "dialog-label")
        content_area.add(self)
