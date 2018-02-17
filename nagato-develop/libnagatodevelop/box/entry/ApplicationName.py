
from libnagatodevelop.box.entry.Entry import NagatoEntry


class NagatoApplicationName(NagatoEntry):

    def _get_label_text(self):
        return "Application Name"

    def _get_key(self):
        return "app-name"

