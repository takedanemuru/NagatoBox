
from gi.repository import Gtk
from libnagato.util import CssProvider


class NagatoDialogLabel(Gtk.Label):

    def __init__(self, content_area, markup):
        Gtk.Label.__init__(self)
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.set_markup(markup)
        self.set_padding(8, 8)
        CssProvider.set_to_widget(self, "dialog-label-about")
        content_area.add(self)
