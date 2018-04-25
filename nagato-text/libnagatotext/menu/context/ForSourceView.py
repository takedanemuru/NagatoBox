
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Context import NagatoContextCore
from libnagato.menu.Separator import NagatoSeparator
from libnagatotext.menu.sub.RecentPaths import NagatoRecentPaths
from libnagatotext.menu.sub.Schemes import NagatoSchems
from libnagatotext.menu.action.BackgroundImage import NagatoBackgroundImage
from libnagatotext.menu.action.Font import NagatoFont
from libnagatotext.menu.action.ShowLineNumbers import NagatoShowLineNumbers


class NagatoContextMenu(NagatoContextCore):

    def _on_context_menu(self, widget, event):
        if event.button == 2:
            self._raise("YUKI.N > clipboard", "paste")
        # kill default context menu of GtkSourceView.
        if event.button == 3:
            return True

    def _add_gtk_callbacks(self):
        self._parent.connect("button-press-event", self._on_context_menu)

    def _initialize_children(self):
        NagatoItem(self, "New", "YUKI.N > files", "new")
        NagatoItem(self, "Load", "YUKI.N > files", "load")
        NagatoItem(self, "Save", "YUKI.N > files", "save")
        NagatoItem(self, "Save As", "YUKI.N > files", "save as")
        NagatoRecentPaths(self)
        NagatoSeparator(self)
        NagatoItem(self, "Cut", "YUKI.N > clipboard", "cut")
        NagatoItem(self, "Copy", "YUKI.N > clipboard", "copy")
        NagatoItem(self, "Paste", "YUKI.N > clipboard", "paste")
        NagatoSeparator(self)
        NagatoItem(self, "Search and Replace", "YUKI.N > search and replace")
        NagatoSeparator(self)
        NagatoSchems(self)
        NagatoFont(self)
        NagatoShowLineNumbers(self)
        NagatoBackgroundImage(self)
