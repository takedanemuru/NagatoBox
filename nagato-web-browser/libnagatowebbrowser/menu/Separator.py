
from gi.repository import Gtk


class NagatoSeparator(Gtk.SeparatorMenuItem):

    def __init__(self, root_menu):
        Gtk.SeparatorMenuItem.__init__(self)
        self.get_style_context().add_class("menu-item")
        root_menu.append(self)
