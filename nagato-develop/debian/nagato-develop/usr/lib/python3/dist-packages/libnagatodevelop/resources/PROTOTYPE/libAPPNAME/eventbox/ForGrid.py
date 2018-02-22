
from libAPPNAME.eventbox.EventBox import NagatoEventBox as TFEI
from libAPPNAME.Grid import NagatoGrid
from libAPPNAME.menu.context.ForChrome import NagatoContextMenu


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._grid = NagatoGrid(self)
        self._parent.add(self)
