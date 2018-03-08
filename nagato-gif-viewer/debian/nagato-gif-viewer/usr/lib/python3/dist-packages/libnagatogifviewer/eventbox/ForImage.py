
from libnagatogifviewer.eventbox.EventBox import NagatoEventBox as TFEI
from libnagatogifviewer.menu.context.ForLabel import NagatoContextMenu
from libnagatogifviewer.Image import NagatoImage


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._image = NagatoImage(self)
