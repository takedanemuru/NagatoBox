
from gi.repository import Gtk


class NagatoListStore(object):

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

    def refresh_data(self, user_data):
        self._list_store.clear()
        while len(user_data) > 1:
            self._append_data(user_data.popleft())

    def get_model(self):
        return self._list_store

    def __init__(self):
        self._list_store = Gtk.ListStore(
            int, str, str, float, str, float, str, float)
