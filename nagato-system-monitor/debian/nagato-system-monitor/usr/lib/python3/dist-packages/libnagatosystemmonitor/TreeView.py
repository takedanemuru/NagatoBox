
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoTreeView(NagatoObject, Gtk.TreeView):

    def _set_column(self, title, xalign, text_index, sort_index):
        yuki_column = Gtk.TreeViewColumn(
            title=title,
            cell_renderer=Gtk.CellRendererText(xalign=xalign),
            text=text_index
            )
        yuki_column.set_sort_column_id(sort_index)
        yuki_column.set_expand(True)
        self.append_column(yuki_column)

    def _on_enter(self, *args):
        self._raise("YUKI.N > set lock", True)

    def _on_leave(self, *args):
        self._raise("YUKI.N > set lock", False)

    def _set_columns(self):
        self._set_column("pid", 0, 0, 0)
        self._set_column("name", 0, 1, 1)
        self._set_column("usage", 1, 2, 3)
        self._set_column("vsize (MiB)", 1, 4, 5)
        self._set_column("rss (MiB)", 1, 6, 7)

    def _set_signals(self):
        self.connect("enter-notify-event", self._on_enter)
        self.connect("leave-notify-event", self._on_leave)

    def __init__(self, parent, model):
        self._parent = parent
        Gtk.TreeView.__init__(self)
        self.set_model(model)
        self._set_signals()
        self._set_columns()
        self._parent.add(self)
