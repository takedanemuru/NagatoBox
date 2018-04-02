
from libnagatotext.dialog.Warning import NagatoWarning
from libnagatotext.dialog.label.ForNotSaved import NagatoDialogLabel

RESPONSE_CANCEL = 0
RESPONSE_DISCARD = 1
RESPONSE_SAVE = 2


class NagatoWarningNotSaved(NagatoWarning):

    @classmethod
    def call(self):
        yuki_dialog = NagatoWarningNotSaved()
        yuki_response = yuki_dialog.run()
        yuki_dialog.destroy()
        return yuki_response

    def _set_buttons(self):
        self.add_button("Cancel", RESPONSE_CANCEL)
        self.add_button("Discard", RESPONSE_DISCARD)
        self.add_button("Save", RESPONSE_SAVE)

    def _get_label(self):
        return ""

    def _set_contents(self):
        self._label = NagatoDialogLabel(self._content_area)
