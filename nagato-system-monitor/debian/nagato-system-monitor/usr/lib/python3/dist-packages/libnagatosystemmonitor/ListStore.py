
from gi.repository import Gtk

COLUMNS = (int, str, str, float, str, float, str, float)


class NagatoListStore(Gtk.ListStore):

    def _append_data(self, data):
        self.append((
            data["pid"],
            data["comm"],
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
        self.clear()
        while len(user_data) > 0:
            self._append_data(user_data.popleft())

    def set_lock(self, lock):
        self._lock = lock

    def __init__(self, parent):
        self._parent = parent
        self._lock = False
        Gtk.ListStore.__init__(self, *COLUMNS)
