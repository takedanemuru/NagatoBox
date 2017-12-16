
from gi.repository import Gtk
from libnagatowebbrowser.CoreObject import NagatoObject


class NagatoItem(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        self._raise(self._message, self._user_data)

    def __init__(self, parent, label, message, user_data=None, root_menu=None):
        self._parent = parent
        if root_menu is None:
            yuki_root_menu = parent
        else:
            yuki_root_menu = root_menu
        Gtk.MenuItem.__init__(self, label)
        self.connect("activate", self._on_activate)
        self.get_style_context().add_class("menu-item")
        self._message = message
        self._user_data = user_data
        yuki_root_menu.append(self)
