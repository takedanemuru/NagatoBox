
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.TreeView import NagatoTreeView
from libnagatosystemmonitor.ListStoreHandler import NagatoListStoreHandler


class NagatoScrolledWindow(Gtk.ScrolledWindow, NagatoObject):

    def queue(self, data):
        self._list_store.queue(data)

    def _yuki_n_set_lock(self, lock):
        self._list_store.set_lock(lock)

    def __init__(self, parent):
        self._parent = parent
        self._lock = False
        Gtk.ScrolledWindow.__init__(self)
        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.EXTERNAL)
        self.set_vexpand(True)
        self._list_store = NagatoListStoreHandler(self)
        self._tree_view = NagatoTreeView(self, self._list_store.list_store)
