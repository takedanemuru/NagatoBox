
from gi.repository import Gtk
from libnagatodevelop.box.Box import NagatoBox


class NagatoHeaderLabel(NagatoBox):

    def _on_initialize(self, user_data=None):
        yuki_label = Gtk.Label()
        yuki_label.set_text(user_data)
        self.pack_start(yuki_label, True, True, 0)
