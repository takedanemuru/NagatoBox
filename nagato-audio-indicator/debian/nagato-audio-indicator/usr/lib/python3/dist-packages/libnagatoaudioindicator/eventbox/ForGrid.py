
from libnagato.ui.EventBox import NagatoEventBox as TFEI
from libnagatoaudioindicator.ui.Grid import NagatoGrid
from libnagatoaudioindicator.menu.context.ForChrome import NagatoContextMenu


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._grid = NagatoGrid(self)
        self._parent.add(self)
