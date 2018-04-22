
from libnagato.dialog.message.Warning import NagatoWarning
from libnagatotext.dialog import Messages

MESSAGE = Messages.NOT_SAVED
BUTTONS = ["Cancel", "Discard", "Save"]
RESPONSE = (False, True, None)


class NagatoSaveState(object):

    def get_save_state(self):
        if self._saved:
            return True
        yuki_response = NagatoWarning.call(message=MESSAGE, buttons=BUTTONS)
        return RESPONSE[yuki_response]

    def set_state_to_saved(self):
        self._saved = True

    def _on_changed(self, text_buffer):
        self._saved = False

    def __init__(self, text_buffer):
        self._saved = True
        text_buffer.connect("changed", self._on_changed)
