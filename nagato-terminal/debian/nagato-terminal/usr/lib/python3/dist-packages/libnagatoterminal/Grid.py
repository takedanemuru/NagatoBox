
from libnagato.datatype.Rect import NagatoRect
from libnagatoterminal.Notebook import NagatoNotebook
from libnagato.flexgrid.FlexGrid import NagatoFlexGrid


class NagatoGrid(NagatoFlexGrid):

    def _yuki_n_new_vte_to(self, grid_data):
        NagatoNotebook(self, self._automata_new(grid_data), False)
        self.show_all()

    def _inform_number_of_grid_children(self):
        return len(self.get_children())

    def _on_initialize(self):
        NagatoNotebook(self, NagatoRect(0, 0), True)

    def get_current_processes(self):
        yuki_processes = []
        for yuki_child in self.get_children():
            yuki_processes += yuki_child.get_current_processes()
        return yuki_processes
