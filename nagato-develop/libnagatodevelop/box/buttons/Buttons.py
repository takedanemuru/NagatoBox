
from libnagatodevelop.box.Box import NagatoBox
from libnagatodevelop.widget.Button import NagatoButton


class NagatoButtons(NagatoBox):

    def _get_sensitive(self):
        pass

    def _set_left_button(self):
        pass

    def _get_right_button(self):
        pass

    def _on_initialize(self, user_data=None):
        self._model = self._enquiry("YUKI.N > model")
        self._set_left_button()
        self._right_button = self._get_right_button()
        self._right_button.set_sensitive(False)

    def check_sensitive(self):
        self._right_button.set_sensitive(self._get_sensitive())
