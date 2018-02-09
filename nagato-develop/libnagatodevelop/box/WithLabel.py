
from gi.repository import Gtk
from libnagatodevelop.box.Box import NagatoBox


class NagatoWithLabel(NagatoBox):

    def _get_key(self):
        return "DON'T LOOK AT ME."

    def _get_label_text(self):
        return "DON'T LOOK AT ME."

    def _set_label(self):
        yuki_label = Gtk.Label()
        yuki_label.set_text(self._get_label_text())
        yuki_label.set_xalign(0)
        self.pack_start(yuki_label, False, True, 32)
 
    def _set_content(self):
        pass

    def _on_initialize(self, user_data=None):
        self._model = self._enquiry("YUKI.N > model")
        self._set_label()
        self._set_content()
