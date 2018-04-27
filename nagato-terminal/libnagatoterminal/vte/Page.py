
from gi.repository import Vte
from libnagato.Object import NagatoObject
from libnagatoterminal.vte.Vte import NagatoVte
from libnagatoterminal.ProcessWatcher import NagatoProcessWatcher
from libnagatoterminal.vte.TabLabel import NagatoTabLabel


class NagatoPage(Vte.Terminal, NagatoObject):

    def _yuki_n_vte_initialized(self, pid):
        self._watcher = NagatoProcessWatcher(pid)
        self._tab_label.set_title("PID : {}".format(pid))

    def _initialize_first_page(self):
        self._parent.insert_page(self._vte, self._tab_label, -1)
        self._parent.set_tab_reorderable(self._vte, True)
        self._vte.show_all()
        # notebook reject to switch page when children aren't visible.
        self._parent.set_current_page(self._parent.get_n_pages() - 1)

    def _yuki_n_destroy(self):
        if self._watcher.can_close_with_user_response():
            self._vte.destroy()
            self._tab_label.destroy()
            self._raise("YUKI.N > child destroyed")

    def _inform_child_process(self):
        return self._watcher.child

    def _inform_working_directory(self):
        return self._watcher.working_directory

    def __init__(self, parent, is_prime_vte, directory=None):
        self._parent = parent
        self._tab_label = NagatoTabLabel(self, parent)
        self._vte = NagatoVte(self, is_prime_vte, directory)
        self._initialize_first_page()
