
from gi.repository import Gtk
from libnagatoscreenshot.dialog.Warning import NagatoWarning
from libnagatoscreenshot.dialog.label.ForWindowNotFound import (
    NagatoDialogLabel)


class NagatoWindowNotFound(NagatoWarning):

    @classmethod
    def call(self):
        yuki_dialog = NagatoWindowNotFound()
        yuki_response = yuki_dialog.run()
        yuki_dialog.destroy()
        return (yuki_response == Gtk.ResponseType.OK)

    def _set_buttons(self):
        self.add_button("OK", Gtk.ResponseType.OK)

    def _get_label(self):
        return "Info"

    def _set_contents(self):
        self._label = NagatoDialogLabel(self._content_area)
