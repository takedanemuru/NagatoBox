
from gi.repository import Gtk


class NagatoListStoreHandler(object):

    def _append_data(self, data):
        if data["rss"] == 0:
            return
        self._list_store.append((
            data["pid"],
            data["name"],
            "{:.2%}".format(data["usage"]),
            data["usage"],
            "{:.2f}".format(data["vsize"]),
            data["vsize"],
            "{:.2f}".format(data["rss"]),
            data["rss"]
            ))

    def queue(self, user_data):
        if self._lock:
            return
        self._list_store.clear()
        while len(user_data) > 0:
            self._append_data(user_data.popleft())

    def set_lock(self, lock):
        self._lock = lock

    def _get_list_store(self):
        return Gtk.ListStore(int, str, str, float, str, float, str, float)

    def __init__(self, parent):
        self._parent = parent
        self._lock = False
        self._list_store = self._get_list_store()

    @property
    def list_store(self):
        return self._list_store
