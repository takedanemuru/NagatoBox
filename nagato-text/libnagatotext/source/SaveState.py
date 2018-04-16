
from libnagatotext.dialog.WarningNotSaved import NagatoWarningNotSaved

RESPONSE = (False, True, None)


class NagatoSaveState(object):

    def get_save_state(self):
        if self._saved:
            return True
        yuki_response = NagatoWarningNotSaved.call()
        return RESPONSE[yuki_response]

    def set_state_to_saved(self):
        self._saved = True

    def _on_changed(self, text_buffer):
        self._saved = False

    def __init__(self, text_buffer):
        self._saved = True
        text_buffer.connect("changed", self._on_changed)
