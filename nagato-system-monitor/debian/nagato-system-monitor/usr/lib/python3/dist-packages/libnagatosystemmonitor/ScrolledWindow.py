
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.TreeView import NagatoTreeView


class NagatoScrolledWindow(Gtk.ScrolledWindow, NagatoObject):

    def _append_data(self, data):
        yuki_usage = data["usage"]
        yuki_vsize = data["vsize"]/1024/1024
        yuki_rss = data["rss"]/256
        self._list_store.append((
            data["pid"],
            data["name"],
            "{:.2%}".format(yuki_usage),
            yuki_usage,
            "{:.2f}".format(yuki_vsize),
            yuki_vsize,
            "{:.2f}".format(yuki_rss),
            yuki_rss
            ))

    def queue(self, user_data):
        if self._lock:
            return
        self._list_store.clear()
        while len(user_data) > 0:
            self._append_data(user_data.popleft())

    def _yuki_n_set_lock(self, lock):
        self._lock = lock

    def __init__(self, parent):
        self._parent = parent
        self._lock = False
        Gtk.ScrolledWindow.__init__(self)
        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.EXTERNAL)
        self.set_vexpand(True)
        self._list_store = Gtk.ListStore(
            int, str, str, float, str, float, str, float)
        self._tree_view = NagatoTreeView(self, self._list_store)
