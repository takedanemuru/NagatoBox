
from libnagatodevelop.box.entry.Entry import NagatoEntry


class NagatoApplicationUri(NagatoEntry):

    def _get_label_text(self):
        return "Application Web Site"

    def _get_key(self):
        return "app-uri"
