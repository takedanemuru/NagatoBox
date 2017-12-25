
from gi.repository import Gtk
from libnagatoterminal.Resources import NagatoResources

class NagatoLabelAbout(Gtk.Label):

    def _get_message(self):
        yuki_resources = NagatoResources()
        return yuki_resources["long-description"]

    def __init__(self, content_area):
        Gtk.Label.__init__(self)
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.get_style_context().add_class("dialog-label-about")
        self.set_markup(self._get_message())
        content_area.add(self)
