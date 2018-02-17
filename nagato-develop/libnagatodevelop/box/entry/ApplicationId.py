
from libnagato.util import CssProvider
from libnagatodevelop.box.entry.Entry import NagatoEntry


class NagatoApplicationId(NagatoEntry):

    def _get_label_text(self):
        return "Application ID"

    def _get_key(self):
        return "app-id"

    def _on_set_css(self):
        CssProvider.set_to_widget(self, "shade-half")
