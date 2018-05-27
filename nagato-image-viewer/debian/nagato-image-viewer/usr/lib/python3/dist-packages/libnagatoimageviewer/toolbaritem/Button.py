
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.util import CssProvider

ICON_SIZE = Gtk.IconSize.LARGE_TOOLBAR


class NagatoButton(Gtk.Button, NagatoObject):

    def _on_activate(self, *args):
        self._raise(self._message, self._user_data)

    def _get_image(self, icon_name):
        return Gtk.Image.new_from_icon_name(icon_name, ICON_SIZE)

    def __init__(self, parent, icon_name, message, icon_name_as_data=False):
        self._parent = parent
        self._message = message
        self._user_data = icon_name if icon_name_as_data else None
        Gtk.Button.__init__(self)
        CssProvider.set_to_widget(self, "button-for-toolbar")
        self.set_image(self._get_image(icon_name))
        self.connect("clicked", self._on_activate)
        self._parent.pack_start(self, False, True, 0)
