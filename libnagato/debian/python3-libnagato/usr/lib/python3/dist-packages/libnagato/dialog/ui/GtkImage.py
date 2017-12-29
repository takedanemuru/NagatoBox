
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from libnagato.util import CssProvider


class NagatoGtkImage(Gtk.Image):

    def __init__(self, container, pixbuf, css, height, width):
        self = Gtk.Image.new_from_pixbuf(pixbuf)
        CssProvider.set_to_widget(self, css)
        self.set_size_request(height, width)
        container.add(self)
