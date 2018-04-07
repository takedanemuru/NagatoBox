
from gi.repository import Gtk
from libnagatodevelop.box.Box import NagatoBox


class NagatoSpacerExpand(NagatoBox):

    def _on_initialize(self, user_data=None):
        yuki_label = Gtk.Label()
        yuki_label.set_text("")
        self.pack_start(yuki_label, True, True, 0)

    def _on_set_css(self):
        self.set_vexpand(True)
