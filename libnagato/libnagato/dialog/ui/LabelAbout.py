
from gi.repository import Gtk
from libnagato.util import CssProvider
from libnagato.Ux import Unit

TEMPLATE = \
    "<span size='x-large'>{}</span>\n"\
    "version: {}\n"\
    "\n"\
    "{}"\
    "\n"\
    "{}"


class NagatoLabelAbout(Gtk.Label):

    def _get_message(self):
        return TEMPLATE.format(
            self._resources["name"],
            self._resources["version"],
            self._resources["long-description"],
            self._resources["authors"]
            )

    def __init__(self, content_area, resources):
        Gtk.Label.__init__(self)
        self._resources = resources
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.set_padding(Unit(1), Unit(1))
        CssProvider.set_to_widget(self, "dialog-label-about")
        self.set_markup(self._get_message())
        content_area.add(self)
