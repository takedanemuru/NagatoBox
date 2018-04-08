
from gi.repository import Gdk
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Context import NagatoContextCore
from libnagato.menu.Separator import NagatoSeparator
from libnagatotext.menu.sub.Schemes import NagatoSchems


class NagatoContextMenu(NagatoContextCore):

    def _on_context_menu(self, widget, event):
        # this method simply returns True to abort default context menu.
        if event.button == 3:
            return True

    def _add_gtk_callbacks(self):
        self._parent.connect("button-press-event", self._on_context_menu)

    def _initialize_children(self):
        NagatoItem(self, "Cut", "YUKI.N > clipboard", "cut")
        NagatoItem(self, "Copy", "YUKI.N > clipboard", "copy")
        NagatoItem(self, "Paste", "YUKI.N > clipboard", "paste")
        NagatoSeparator(self)
        NagatoSchems(self)
