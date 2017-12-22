
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatoterminal.Vte import NagatoVte
from libnagatoterminal.NotebookPosition import NagatoNotebookPosition
from libnagatoterminal.TabVisibility import NagatoTabVisibility
from libnagatoterminal.datatype.UnnullableArray import NagatoUnnullableArray


class NagatoNotebook(NagatoObject, Gtk.Notebook):

    def _yuki_n_add_new_tab(self, working_directory_uri=None):
        NagatoVte(self, False, working_directory_uri)

    def _yuki_n_child_destroyed(self):
        if len(self.get_children()) == 0:
            self.destroy()
            self._raise("YUKI.N > child destroyed")

    def _inform_new_vte_rect(self, gtk_position_type):
        return self._position.get_new_vte_rect(gtk_position_type)

    def _inform_expanded_rect(self, gtk_position_type):
        return self._position.get_expanded_rect(gtk_position_type)

    def _inform_shrinked_rect(self, gtk_position_type):
        return self._position.get_shrinked_rect(gtk_position_type)

    def _inform_can_shrink_to(self, gtk_position_type):
        return self._position.can_shrink_to(gtk_position_type)

    def _inform_notebook_itself(self):
        return self

    def adjust_position(self, gtk_position_type, rect):
        self._position.adjust(gtk_position_type, rect)

    def move_to(self, rect):
        self._position.move_to(rect)

    def get_current_processes(self):
        yuki_processes = NagatoUnnullableArray()
        for yuki_page in self.get_children():
            yuki_processes.append(yuki_page.child_process)
        return yuki_processes.data

    def __init__(self, parent, is_prime_vte, rect):
        self._parent = parent
        self._position = NagatoNotebookPosition(rect.left, rect.top)
        Gtk.Notebook.__init__(self)
        self.set_scrollable(True)
        parent.attach(self, rect.left, rect.top, 1, 1)
        NagatoTabVisibility(self)
        NagatoVte(self, is_prime_vte)
