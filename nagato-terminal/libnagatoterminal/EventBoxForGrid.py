
from gi.repository import Gdk
from libnagatoterminal.EventBox import NagatoEventBox as TFEI
from libnagatoterminal.menu.context.ForChrome import NagatoContextMenu
from libnagatoterminal.Grid import NagatoGrid
from libnagatoterminal.dialog import Portal


class NagatoEventBox(TFEI):

    def can_close(self):
        yuki_processes = self._grid.get_current_processes()
        return Portal.get_can_close_window(yuki_processes)

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._grid = NagatoGrid(self)
        self._parent.add(self)
        self.set_above_child(False)
