
from gi.repository import Gtk
from libnagato.util import CssProvider


TEMPLATE = \
    "\n"\
    "Screenshot successfully saved to\n"\
    "\n"\
    "{}\n"\
    "\n"


class NagatoDialogLabel(Gtk.Label):

    def _get_markup(self):
        return TEMPLATE.format(self._user_data)

    def __init__(self, content_area, user_data):
        Gtk.Label.__init__(self)
        self._user_data = user_data
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.set_markup(self._get_markup())
        self.set_padding(8, 8)
        CssProvider.set_to_widget(self, "dialog-label-about")
        content_area.add(self)
