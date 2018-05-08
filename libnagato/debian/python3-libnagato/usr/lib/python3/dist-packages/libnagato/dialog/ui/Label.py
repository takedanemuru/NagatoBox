
from gi.repository import Gtk
from libnagato.Ux import Unit
from libnagato.util import CssProvider


class NagatoLabel(Gtk.Label):

    def __init__(self, content_area, markup, css):
        Gtk.Label.__init__(self)
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.set_markup(markup)
        self.set_padding(Unit(1), Unit(1))
        CssProvider.set_to_widget(self, css)
        content_area.add(self)
