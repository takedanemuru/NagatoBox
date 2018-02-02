
from libnagatowebbrowser.EventBox import NagatoEventBox as TFEI
from libnagatowebbrowser.Grid import NagatoGrid
from libnagatowebbrowser.menu.context.ForChrome import NagatoContextMenu


class NagatoEventBox(TFEI):

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._grid = NagatoGrid(self)
        self._parent.add(self)
