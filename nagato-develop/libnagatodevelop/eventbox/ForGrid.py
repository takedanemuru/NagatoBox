
from libnagato.ui.EventBox import NagatoEventBox as TFEI
from libnagatodevelop.Grid import NagatoGrid
from libnagatodevelop.menu.context.ForChrome import NagatoContextMenu


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._grid = NagatoGrid(self)
        self._parent.add(self)
