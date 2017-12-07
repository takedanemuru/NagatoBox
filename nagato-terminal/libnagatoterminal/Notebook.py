
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.Vte2 import NagatoVte
from libnagatoterminal.GridPosition import NagatoGridPosition
from libnagatoterminal.TabVisibility import NagatoTabVisibility


class NagatoNotebook(NagatoObject, Gtk.Notebook):

    def _yuki_n_new_vte_to(self, user_data):
        yuki_rect = self._position.get_new_vte_rect(user_data)
        self._raise("YUKI.N > new vte to", (self, user_data, yuki_rect))
        
    def _yuki_n_expand_to(self, user_data):
        yuki_rect = self._position.get_expanded_rect(user_data)
        self._raise("YUKI.N > expand to", (self, user_data, yuki_rect))
        
    def _yuki_n_shrink_to(self, user_data):
        if not self._position.can_shrink_to(user_data):
            return
        yuki_rect = self._position.get_shrinked_rect(user_data)
        self._raise("YUKI.N > shrink to", (self, user_data, yuki_rect))

    def _yuki_n_add_new_tab(self, user_data=None):
        NagatoVte(self, False, user_data)

    def _yuki_n_child_destroyed(self):
        if len(self.get_children()) == 0:
            self.destroy()
            self._raise("YUKI.N > child destroyed")

    def _inform_can_shrink_to(self, user_data):
        return self._position.can_shrink_to(user_data)

    def adjust_position(self, gtk_position_type, rect):
        self._position.adjust(gtk_position_type, rect)

    def move_to(self, rect):
        self._position.move_to(rect)

    def __init__(self, parent, is_prime_vte, rect):
        self._parent = parent
        self._position = NagatoGridPosition(rect.left, rect.top)
        Gtk.Notebook.__init__(self)
        self.set_scrollable(True)
        parent.attach(self, rect.left, rect.top, 1, 1)
        NagatoTabVisibility(self)
        NagatoVte(self, is_prime_vte)

    def get_current_processes(self):
        yuki_processes = []
        for yuki_page in self.get_children():
            yuki_process = yuki_page.child_process
            if yuki_process is not None:
                yuki_processes.append(yuki_process)
        return yuki_processes
