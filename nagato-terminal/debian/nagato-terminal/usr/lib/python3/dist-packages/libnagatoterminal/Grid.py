
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.GridAttributes import NagatoGridAttributes
from libnagatoterminal.Notebook import NagatoNotebook
from libnagatoterminal.automata.grid.New import NagatoNew
from libnagatoterminal.automata.grid.Expand import NagatoExpand


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _move_to(self, notebook, rect):
        self.remove(notebook)
        self.attach(notebook, rect.left, rect.top, rect.width, rect.height)
        notebook.move_to(rect)
        self.show_all()

    def _yuki_n_new_vte_to(self, grid_data):
        NagatoNotebook(self, False, self._automata_new(grid_data))
        self.show_all()

    def _yuki_n_expand_to(self, grid_data):
        self._move_to(grid_data.signal_from, self._automata_expand(grid_data))

    def _yuki_n_shrink_to(self, grid_data):
        self._move_to(grid_data.signal_from, grid_data.destination_rect)

    def _yuki_n_child_destroyed(self):
        if len(self.get_children()) == 0:
            self._raise("YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        Gtk.Grid.__init__(self)
        NagatoGridAttributes(self)
        self._automata_new = NagatoNew(self)
        self._automata_expand = NagatoExpand(self)
        NagatoNotebook(self, True, NagatoRect(0, 0))
        self._parent.add(self)

    def get_current_processes(self):
        yuki_processes = []
        for yuki_child in self.get_children():
            yuki_processes += yuki_child.get_current_processes()
        return yuki_processes
