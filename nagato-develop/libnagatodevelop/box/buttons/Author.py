
from libnagatodevelop.box.buttons.Buttons import NagatoButtons as TFEI
from libnagatodevelop.widget.Button import NagatoButton

CSS = "button-test"
KEYS = {
    "user-name",
    "user-email",
    "user-uri",
    "user-id"
}


class NagatoButtons(TFEI):

    def _get_sensitive(self):
        for yuki_key in KEYS:
            if self._model[yuki_key] == "":
                return False
        return True

    def _set_left_button(self):
        NagatoButton(self, "Calcel", "YUKI.N > quit", CSS)

    def _get_right_button(self):
        return NagatoButton(self, "Next", "YUKI.N > go to application", CSS)
