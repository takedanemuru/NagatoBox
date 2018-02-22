

from gi.repository import Gtk
from libnagatodevelop.box.Box import NagatoBox
from libnagato.util import CssProvider


class NagatoDescriptionLabel(NagatoBox):

    def _on_initialize(self, user_data=None):
        yuki_label = Gtk.Label()
        yuki_label.set_text(user_data)
        yuki_label.set_alignment(0, 0.5)
        CssProvider.set_to_widget(yuki_label, "shade-full")
        self.pack_start(yuki_label, True, True, 8)
