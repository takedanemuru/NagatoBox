
from gi.repository import Gtk
from gi.repository import Gdk
from libnagato.Object import NagatoObject


class NagatoTreeView(Gtk.ScrolledWindow, NagatoObject):

    def queue(self, user_data):
        self._list_store.clear()
        while len(user_data) > 0:
            yuki_data = user_data.popleft()
            self._list_store.append((
                yuki_data["pid"],
                yuki_data["name"],
                "{:.2%}".format(yuki_data["usage"]),
                yuki_data["usage"],
                "{:.2f}".format(yuki_data["vsize"]/1024/1024),
                "{:.2f}".format(yuki_data["rss"]/256),
                yuki_data["vsize"]/1024/1024,
                yuki_data["rss"]/256
                ))
        self._lock = False

    def _set_column(self, title, xalign, text_index, sort_index):
        yuki_column = Gtk.TreeViewColumn(
            title,
            Gtk.CellRendererText(xalign=xalign),
            text=text_index
            )
        yuki_column.set_sort_column_id(sort_index)
        yuki_column.set_expand(True)
        self._tree_view.append_column(yuki_column)

    def _on_draw(self, *args):
        if self._lock:
            return False
        self._lock = True
        return True

    def _initialize_tree_view(self):
        self._tree_view = Gtk.TreeView(model=self._list_store)
        self._tree_view.connect("draw", self._on_draw)
        self._set_column("pid", 0, 0, 0)
        self._set_column("name", 0, 1, 1)
        self._set_column("usage", 1, 2, 3)
        self._set_column("vsize (MiB)", 1, 4, 6)
        self._set_column("rss (MiB)", 1, 5, 7)

    def __init__(self, parent):
        self._parent = parent
        self._lock = False
        Gtk.ScrolledWindow.__init__(self)
        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.set_vexpand(True)
        self._list_store = Gtk.ListStore(
            int, str, str, float, str, str, float, float)
        self._initialize_tree_view()
        self.add(self._tree_view)
