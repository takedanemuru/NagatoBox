
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.FlexGridAttributes import NagatoFlexGridAttributes
from libnagatoterminal.flexgrid.adjust.New import NagatoNew
from libnagatoterminal.flexgrid.adjust.Expand import NagatoExpand


class NagatoFlexGrid(Gtk.Grid, NagatoObject):

    def _move_to(self, child, rect):
        self.remove(child)
        self.attach(child, rect.left, rect.top, rect.width, rect.height)
        child.move_to(rect)
        self.show_all()

    def _yuki_n_expand_to(self, grid_data):
        yuki_destination_rect = self._automata_expand(grid_data)
        self._move_to(grid_data.signal_from, yuki_destination_rect)

    def _yuki_n_shrink_to(self, grid_data):
        self._move_to(grid_data.signal_from, grid_data.destination_rect)

    def _yuki_n_child_destroyed(self):
        if len(self.get_children()) == 0:
            self._raise("YUKI.N > quit")

    def _get_rect_for_new_child(self, grid_data):
        return self._automata_new(grid_data)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Grid.__init__(self)
        NagatoFlexGridAttributes(self)
        self._automata_new = NagatoNew(self)
        self._automata_expand = NagatoExpand(self)
        self._on_initialize()
        self._parent.add(self)
