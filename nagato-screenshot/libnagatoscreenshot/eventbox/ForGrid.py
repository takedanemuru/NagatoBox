
from libnagatoscreenshot.eventbox.EventBox import NagatoEventBox as TFEI
from libnagatoscreenshot.Grid import NagatoGrid
from libnagatoscreenshot.menu.context.ForChrome import NagatoContextMenu


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._grid = NagatoGrid(self)
        self._parent.add(self)
