
from gi.repository import Gtk
from gi.repository import Gdk
from libnagatoterminal.CoreObject import NagatoObject


class NagatoPaste(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        self._raise("YUKI.N > paste")

    def _on_draw(self, widget, cr):
        yuki_clipboard = Gtk.Clipboard.get_default(Gdk.Display.get_default())
        self.set_sensitive(yuki_clipboard.wait_is_text_available())

    def __init__(self, parent):
        self._parent = parent
        Gtk.MenuItem.__init__(self, "Paste")
        self.connect("activate", self._on_activate)
        self.connect("draw", self._on_draw)
        self._parent.append(self)        

