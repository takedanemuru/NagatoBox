
from gi.repository import Gtk
from libnagatowebbrowser.CoreObject import NagatoObject


class NagatoButtonClose(NagatoObject):

    def _on_activate(self, widget):
        self._raise("YUKI.N > request close tab")

    def __init__(self, parent):
        self._parent = parent
        self._button = Gtk.Button.new_from_icon_name(
            "window-close-symbolic",
            Gtk.IconSize.BUTTON
            )
        self._button.connect("clicked", self._on_activate)
        self._parent.pack_start(self._button, True, False, 0)
