
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.Vte2 import NagatoVte
from libnagatoterminal.GridPosition import NagatoGridPosition


class NagatoNotebook(NagatoObject, Gtk.Notebook):

    def _on_order_changed(self, notebook, child, page_num):
        self.set_show_tabs(self.get_n_pages() > 1)

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

    def _yuki_n_add_new_tab(self):
        NagatoVte(self, False)

    def _yuki_n_child_destroyed(self):
        if len(self.get_children()) == 0:
            self.destroy()
            self._raise("YUKI.N > child destroyed")

    def _set_callbacks(self):
        self.connect("page-added", self._on_order_changed)
        self.connect("page-reordered", self._on_order_changed)
        self.connect("page-removed", self._on_order_changed)

    def adjust_position(self, gtk_position_type, rect):
        self._position.adjust(gtk_position_type, rect)

    def move_to(self, rect):
        self._position.move_to(rect)

    def __init__(self, parent, is_prime_vte, rect):
        self._parent = parent
        self._position = NagatoGridPosition(rect.left, rect.top)
        Gtk.Notebook.__init__(self)
        self.set_opacity(0.7)
        self.set_scrollable(True)
        parent.attach(self, rect.left, rect.top, 1, 1)
        self._set_callbacks()
        NagatoVte(self, is_prime_vte)

    @property
    def can_close_all_chilren(self):
        for yuki_page in self.get_children():
            if not yuki_page.can_close:
                return False
        return True
