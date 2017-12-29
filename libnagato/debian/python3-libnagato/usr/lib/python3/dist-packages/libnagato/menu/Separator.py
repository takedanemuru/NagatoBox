
from gi.repository import Gtk


class NagatoSeparator(object):

    def __init__(self, parent):
        parent.append(Gtk.SeparatorMenuItem())
