
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoInPageSearch(Gtk.ActionBar, NagatoObject):

    def _on_initialize(self):
        self._close_button = Gtk.Button(label="Close")
        self.pack_start(self._close_button)
        self._search_box = Gtk.SearchEntry()
        self._next_button = Gtk.Button(label="Next")
        self.pack_end(self._next_button)
        self._previous_button = Gtk.Button(label="Prev")
        self.pack_end(self._previous_button)
        self._search_box.set_hexpand(True)
        self._search_box.set_placeholder_text("Input Text to Find...")
        self.pack_end(self._search_box)

    def toggle(self):
        if self.get_visible():
            self.hide()
        else:
            self.show()

    def __init__(self, parent):
        # parent MUST be a Gtk.Box
        self._parent = parent
        Gtk.ActionBar.__init__(self)
        self.set_hexpand(True)
        self._parent.pack_end(self, False, False, 0)
        self.set_size_request(0, 32)
        self._on_initialize()
