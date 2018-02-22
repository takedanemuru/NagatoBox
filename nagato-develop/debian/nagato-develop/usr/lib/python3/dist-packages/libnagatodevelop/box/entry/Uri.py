
from libnagatodevelop.box.entry.Entry import NagatoEntry


class NagatoUri(NagatoEntry):

    def _get_label_text(self):
        return "Web Site"

    def _get_key(self):
        return "user-uri"
