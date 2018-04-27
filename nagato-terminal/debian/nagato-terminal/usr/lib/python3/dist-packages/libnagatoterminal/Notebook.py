
from gi.repository import Gtk
from libnagato.ui.NotebookTabVisibility import NagatoTabVisibility
from libnagato.datatype.UnnullableArray import NagatoUnnullableArray
from libnagatoterminal.vte.Page import NagatoPage
from libnagato.flexgrid.Container import NagatoContainer


class NagatoNotebook(NagatoContainer, Gtk.Notebook):

    def _yuki_n_add_new_tab(self, working_directory_uri=None):
        NagatoPage(self, False, working_directory_uri)

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

    def _on_initialize(self, rect, is_prime_vte):
        Gtk.Notebook.__init__(self)
        self.set_scrollable(True)
        self.set_can_focus(False)
        NagatoTabVisibility(self)
        NagatoPage(self, is_prime_vte)
