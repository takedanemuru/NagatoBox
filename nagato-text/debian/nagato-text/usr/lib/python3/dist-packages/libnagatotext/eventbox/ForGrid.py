
from libnagatotext.eventbox.EventBox import NagatoEventBox as TFEI
from libnagatotext.Grid import NagatoGrid
from libnagatotext.menu.context.ForChrome import NagatoContextMenu


class NagatoEventBox(TFEI):

    def _yuki_n_to_source_view(self, message):
        self._grid.prime_call("YUKI.N > {}".format(message))

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._grid = NagatoGrid(self)
        self._parent.add(self)