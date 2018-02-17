
from gi.repository import Gtk
from libnagatodevelop.box.WithLabel import NagatoWithLabel


class NagatoEntry(NagatoWithLabel):

    def _on_changed(self, editable):
        self._model[self._get_key()] = editable.get_text()
        self._raise("YUKI.N > entry changed", self._get_key())

    def _addtional_setups(self):
        pass

    def _set_content(self):
        self._entry = Gtk.Entry()
        self._entry.set_text(self._model[self._get_key()])
        self._entry.connect("changed", self._on_changed)
        self._addtional_setups()
        self.pack_end(self._entry, False, True, 8)

    def set_text(self, text):
        self._entry.set_text(text)
