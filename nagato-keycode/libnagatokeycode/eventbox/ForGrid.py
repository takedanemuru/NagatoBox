
from libnagatokeycode.eventbox.EventBox import NagatoEventBox as TFEI
from libnagatokeycode.Grid import NagatoGrid
from libnagatokeycode.menu.context.ForChrome import NagatoContextMenu


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._grid = NagatoGrid(self)
        self._parent.add(self)
