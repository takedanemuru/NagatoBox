
from libnagatodevelop.box.buttons.Buttons import NagatoButtons as TFEI
from libnagatodevelop.widget.Button import NagatoButton


class NagatoButtons(TFEI):

    def _set_left_button(self):
        NagatoButton(self, "Back", "YUKI.N > back", "button-test")

    def _get_right_button(self):
        return NagatoButton(self, "Create", "YUKI.N > create","button-test")

    def check_sensitive(self):
        pass

