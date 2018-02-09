
from libnagatodevelop.box.Box import NagatoBox
from libnagatodevelop.widget.Button import NagatoButton


class NagatoButtons(NagatoBox):

    def _set_left_button(self):
        pass

    def _get_right_button(self):
        pass

    def _on_initialize(self, user_data=None):
        self._config = self._raise("YUKI.N > model")
        self._set_left_button()
        self._right_button = self._get_right_button()

    def check_sensitive(self):
        pass

