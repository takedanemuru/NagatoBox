
from libnagatodevelop.box.entry.Entry import NagatoEntry


class NagatoUserName(NagatoEntry):

    def _get_label_text(self):
        return "User Name"

    def _get_key(self):
        return "user-name"
