
from libnagatogifviewer.eventbox.EventBox import NagatoEventBox as TFEI
from libnagatogifviewer.Grid import NagatoGrid
from libnagatogifviewer.menu.context.ForChrome import NagatoContextMenu


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._grid = NagatoGrid(self)
        self._parent.add(self)
