
from gi.repository import Gtk
from libAPPNAME.dialog.Warning import NagatoWarning
from libAPPNAME.dialog.label.ForWarningQuit import NagatoDialogLabel


class NagatoWarningQuit(NagatoWarning):

    @classmethod
    def call(self):
        yuki_dialog = NagatoWarningQuit()
        yuki_response = yuki_dialog.run()
        yuki_dialog.destroy()
        return (yuki_response == Gtk.ResponseType.OK)

    def _set_buttons(self):
        self.add_button("Cancel", Gtk.ResponseType.CANCEL)
        self.add_button("Close", Gtk.ResponseType.OK)

    def _get_label(self):
        return "quit ?"

    def _set_contents(self):
        self._label = NagatoDialogLabel(self._content_area)
