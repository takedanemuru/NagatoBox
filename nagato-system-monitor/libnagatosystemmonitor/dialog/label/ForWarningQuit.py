
from gi.repository import Gtk
from libnagato.util import CssProvider


TEMPLATE = \
    "<span size='large'><u>WARNING !!</u></span>\n"\
    "\n"\
    "Do you really want to close nagato-system-monitor ?\n"\
    "\n"


class NagatoDialogLabel(Gtk.Label):

    def __init__(self, content_area):
        Gtk.Label.__init__(self)
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.set_markup(TEMPLATE)
        self.set_padding(8, 8)
        CssProvider.set_to_widget(self, "dialog-label") 
        content_area.add(self)
