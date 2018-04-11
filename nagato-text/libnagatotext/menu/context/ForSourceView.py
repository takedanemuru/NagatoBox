
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Context import NagatoContextCore
from libnagato.menu.Separator import NagatoSeparator
from libnagatotext.menu.sub.Schemes import NagatoSchems
from libnagatotext.menu.action.BackgroundImage import NagatoBackgroundImage


class NagatoContextMenu(NagatoContextCore):

    def _on_context_menu(self, widget, event):
        # this method override default context menu of GtkSourceView.
        if event.button == 3:
            return True

    def _add_gtk_callbacks(self):
        self._parent.connect("button-press-event", self._on_context_menu)

    def _initialize_children(self):
        NagatoItem(self, "New", "YUKI.N > to source view", "new")
        NagatoItem(self, "Load", "YUKI.N > to source view", "load")
        NagatoItem(self, "Save", "YUKI.N > to source view", "save")
        NagatoItem(self, "Save As", "YUKI.N > to source view", "save as")
        NagatoSeparator(self)
        NagatoItem(self, "Cut", "YUKI.N > clipboard", "cut")
        NagatoItem(self, "Copy", "YUKI.N > clipboard", "copy")
        NagatoItem(self, "Paste", "YUKI.N > clipboard", "paste")
        NagatoSeparator(self)
        NagatoSchems(self)
        NagatoBackgroundImage(self)
