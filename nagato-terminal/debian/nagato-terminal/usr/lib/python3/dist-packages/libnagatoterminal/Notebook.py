
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatoterminal.Vte import NagatoVte
from libnagato.ui.NotebookTabVisibility import NagatoTabVisibility
from libnagatoterminal.datatype.UnnullableArray import NagatoUnnullableArray
from libnagatoterminal.FlexGridContainer import NagatoFlexGridContainer
from libnagatoterminal.FlexGridPosition import NagatoFlexGridPosition


class NagatoNotebook(NagatoFlexGridContainer, Gtk.Notebook):

    def _yuki_n_add_new_tab(self, working_directory_uri=None):
        NagatoVte(self, False, working_directory_uri)

    def _yuki_n_child_destroyed(self):
        if len(self.get_children()) == 0:
            self.destroy()
            self._raise("YUKI.N > child destroyed")

    def _inform_notebook_itself(self):
        return self

    def get_current_processes(self):
        yuki_processes = NagatoUnnullableArray()
        for yuki_page in self.get_children():
            yuki_processes.append(yuki_page.child_process)
        return yuki_processes.data

    def __init__(self, parent, is_prime_vte, rect):
        self._parent = parent
        self._position = NagatoFlexGridPosition(rect.left, rect.top)
        Gtk.Notebook.__init__(self)
        self.set_scrollable(True)
        NagatoTabVisibility(self)
        NagatoVte(self, is_prime_vte)
        parent.attach(self, rect.left, rect.top, 1, 1)
