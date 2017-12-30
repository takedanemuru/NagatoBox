
from gi.repository import Gtk


class NagatoSeparator(Gtk.SeparatorMenuItem):

    def __init__(self, parent):
        Gtk.SeparatorMenuItem.__init__(self)
        parent.append(self)
