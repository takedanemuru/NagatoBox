
from gi.repository import Gtk
from libnagatoscreenshot.dialog.Info import NagatoInfo
from libnagatoscreenshot.dialog.label.ForSaved import NagatoDialogLabel


class NagatoSaved(NagatoInfo):

    @classmethod
    def call(self, user_data):
        yuki_dialog = NagatoSaved(user_data)
        yuki_response = yuki_dialog.run()
        yuki_dialog.destroy()
        return (yuki_response == Gtk.ResponseType.OK)

    def _set_buttons(self):
        self.add_button("OK", Gtk.ResponseType.OK)

    def _get_label(self):
        return "successfully saved"

    def _set_contents(self):
        self._label = NagatoDialogLabel(self._content_area, self._user_data)

