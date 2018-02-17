
from gi.repository import Gtk
from libnagatodevelop.box.Box import NagatoBox
from libnagato.util import CssProvider


class NagatoSingleEntry(NagatoBox):

    def _get_key(self):
        return "app-short-description"

    def _on_changed(self, editable):
        self._model[self._get_key()] = editable.get_text()
        self._raise("YUKI.N > entry changed", self._get_key())

    def _on_initialize(self, user_data=None):
        self._model = self._enquiry("YUKI.N > model")
        self._entry = Gtk.Entry()
        self._entry.connect("changed", self._on_changed)
        self.pack_start(self._entry, True, True, 0)
