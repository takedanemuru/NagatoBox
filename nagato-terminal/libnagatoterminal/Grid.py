
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.GridAttributes import NagatoGridAttributes
from libnagatoterminal.VteExtGridPosition import NagatoVteExtGridPosition
from libnagatoterminal.GridAutomataVteNew import NagatoGridAutomataVteNew
from libnagatoterminal.GridAutomataVteExpand import NagatoGridAutomataVteExpand


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _move_to(self, vte, rect):
        self.remove(vte)
        self.attach(vte, rect.left, rect.top, rect.width, rect.height)
        vte.move_to(rect)
        self.show_all()

    def _yuki_n_new_vte_to(self, user_data):
        yuki_rect = self._automata_vte_new(user_data)
        NagatoVteExtGridPosition(self, False, yuki_rect)
        self.show_all()

    def _yuki_n_expand_to(self, user_data):
        yuki_rect = self._automata_vte_expand(user_data)
        self._move_to(user_data[0], yuki_rect)

    def _yuki_n_shrink_to(self, user_data):
        self._move_to(user_data[0], user_data[2])

    def _yuki_n_child_destroyed(self):
        if len(self.get_children()) == 0:
            self._raise("YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        Gtk.Grid.__init__(self)
        NagatoGridAttributes(self)
        self._automata_vte_new = NagatoGridAutomataVteNew(self)
        self._automata_vte_expand = NagatoGridAutomataVteExpand(self)
        NagatoVteExtGridPosition(self, True, NagatoRect(0, 0))

    @property
    def can_close_all_chilren(self):
        for yuki_vte in self.get_children():
            if not yuki_vte.can_close:
                return False
        return True
