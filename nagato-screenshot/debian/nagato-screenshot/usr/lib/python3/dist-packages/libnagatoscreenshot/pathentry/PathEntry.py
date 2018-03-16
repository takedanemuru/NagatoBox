
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.util import CssProvider


class NagatoPathEntry(NagatoObject):

    def _on_map(self, *args):
        print("YUKI.N > DON'T LOOK AT ME.")

    def _on_changed(self, editable):
        self._raise(self._get_message(), self._entry.get_text())

    def _get_label(self):
        return "YUKI.N > DON'T LOOK AT ME."

    def _get_message(self):
        return "YUKI.N > DON'T LOOK AT ME."

    def _set_label(self, x, y):
        self._label = Gtk.Label(self._get_label())
        CssProvider.set_to_widget(self._label, "path-label")
        self._label.set_padding(8, 0)
        self._parent.attach(self._label, x, y, 1, 1)

    def _set_entry(self, x, y):
        self._entry = Gtk.Entry()
        self._parent.attach(self._entry, x+1, y, 2, 1)
        self._entry.connect("map", self._on_map)
        self._entry.connect("changed", self._on_changed)

    def __init__(self, parent, x, y):
        self._parent = parent
        self._set_label(x, y)
        self._set_entry(x, y)

    @property
    def text(self):
        return self._label.get_text()
