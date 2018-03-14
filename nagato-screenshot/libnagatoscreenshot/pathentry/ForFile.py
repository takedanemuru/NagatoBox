
from datetime import datetime
from libnagatoscreenshot.pathentry.PathEntry import NagatoPathEntry as TFEI


class NagatoPathEntry(TFEI):

    def _get_message(self):
        return "YUKI.N > file name changed"

    def _on_map(self, *args):
        yuki_time_stamp = self._enquiry("YUKI.N > time stamp")
        self._entry.set_text(yuki_time_stamp+".png")

    def _get_label(self):
        return "File Name : "
