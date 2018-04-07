
from gi.repository import Gtk
from libnagatodevelop.box.DescriptionLabel import NagatoDescriptionLabel
from libnagatodevelop.group.Group import NagatoGroup

LONG = "Long Description : "


class NagatoLongDescription(NagatoGroup):

    def _get_key(self):
        return "app-long-description"

    def _on_changed(self, text_buffer):
        self._model[self._get_key()] = text_buffer.get_property("text")
        self._raise("YUKI.N > entry changed", self._get_key())

    def _initialize_text_view(self):
        self._text_view = Gtk.TextView()
        self._text_view.set_hexpand(True)
        self._text_view.set_wrap_mode(Gtk.WrapMode.WORD)
        self._buffer = self._text_view.get_buffer()
        self._buffer.connect("changed", self._on_changed)

    def _set_contents(self):
        self._scrolled_window = Gtk.ScrolledWindow()
        self._scrolled_window.set_size_request(-1, 240)
        self._initialize_text_view()
        self._scrolled_window.add(self._text_view)
        self.pack_start(NagatoDescriptionLabel(self, LONG), False, False, 0)
        self.pack_start(self._scrolled_window, True, True, 0)

    def _on_initialize(self):
        self._model = self._enquiry("YUKI.N > model")
        self._set_contents()
