
from gi.repository import Gtk
from libnagato.util import CssProvider
from libAPPNAME.eventbox.EventBox import NagatoEventBox as TFEI
from libAPPNAME.menu.context.ForLabel import NagatoContextMenu


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._label = Gtk.Label()
        self._label.set_vexpand(True)
        self._label.set_hexpand(True)
        self._label.set_text("YUKI.N > 見えてる？")
        CssProvider.set_to_widget(self._label, "dummy-label")
        self.add(self._label)
