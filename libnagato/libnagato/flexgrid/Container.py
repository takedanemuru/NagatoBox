
from libnagato.Object import NagatoObject
from libnagato.flexgrid.Position import NagatoPosition


class NagatoContainer(NagatoObject):

    def _inform_new_vte_rect(self, gtk_position_type):
        return self._position.get_new_vte_rect(gtk_position_type)

    def _inform_expanded_rect(self, gtk_position_type):
        return self._position.get_expanded_rect(gtk_position_type)

    def _inform_shrinked_rect(self, gtk_position_type):
        return self._position.get_shrinked_rect(gtk_position_type)

    def _inform_can_shrink_to(self, gtk_position_type):
        return self._position.can_shrink_to(gtk_position_type)

    def _inform_can_shrink(self):
        return self._position.can_shrink()

    def _inform_flex_grid_container_itself(self):
        return self

    def adjust_position(self, gtk_position_type, rect):
        self._position.adjust(gtk_position_type, rect)

    def move_to(self, rect):
        self._position.move_to(rect)

    def __init__(self, parent, rect, user_data):
        self._parent = parent
        self._position = NagatoPosition(rect.left, rect.top)
        self._on_initialize(rect, user_data)
        parent.attach(self, rect.left, rect.top, rect.height, rect.width)
