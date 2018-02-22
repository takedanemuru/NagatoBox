
from libnagato.util import CssProvider
from libnagatodevelop.box.entry.Entry import NagatoEntry


class NagatoMailAddress(NagatoEntry):

    def _get_label_text(self):
        return "E-Mail Address"

    def _on_set_css(self):
        CssProvider.set_to_widget(self, "shade-half")

    def _get_key(self):
        return "user-email"
