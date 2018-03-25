
from libnagatosystemmonitor.eventbox.EventBox import NagatoEventBox as TFEI
from libnagatosystemmonitor.Grid import NagatoGrid
from libnagatosystemmonitor.menu.context.ForChrome import NagatoContextMenu


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._grid = NagatoGrid(self)
        self._parent.add(self)
