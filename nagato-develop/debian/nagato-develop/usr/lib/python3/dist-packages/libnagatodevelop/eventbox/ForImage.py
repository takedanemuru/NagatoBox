
from libnagatodevelop.eventbox.EventBox import NagatoEventBox as TFEI
from libnagatodevelop.box.Icon import NagatoIcon


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        self._icon = NagatoIcon(self)
        self.add(self._icon)
