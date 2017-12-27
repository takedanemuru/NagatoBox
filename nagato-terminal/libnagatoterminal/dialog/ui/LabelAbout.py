
from gi.repository import Gtk
from libnagatoterminal.Resources import NagatoResources

TEMPLATE = \
    "<span size='x-large'>{}</span>\n"\
    "version: {}\n"\
    "\n"\
    "{}"\
    "\n"\
    "{}"


class NagatoLabelAbout(Gtk.Label):

    def _get_message(self):
        yuki_resources = NagatoResources()
        return TEMPLATE.format(
            yuki_resources["name"],
            yuki_resources["version"],
            yuki_resources["long-description"],
            yuki_resources["authers"]
            )

    def __init__(self, content_area):
        Gtk.Label.__init__(self)
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.get_style_context().add_class("dialog-label-about")
        self.set_markup(self._get_message())
        content_area.add(self)
