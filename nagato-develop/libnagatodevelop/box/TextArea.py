
from gi.repository import Gtk
from libnagatodevelop.box.Box import NagatoBox

BORDER_WIDTH = 8


class NagatoTextArea(NagatoBox):

    def _on_initialize(self, user_data=None):
        self._text_view = Gtk.TextView()
        self._text_view.set_border_width(BORDER_WIDTH)
        self.pack_start(self._text_view, True, True, 0)
