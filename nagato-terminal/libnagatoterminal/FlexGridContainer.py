
from libnagato.Object import NagatoObject
from libnagatoterminal.FlexGridPosition import NagatoFlexGridPosition


class NagatoFlexGridContainer(NagatoObject):

    def _inform_new_vte_rect(self, gtk_position_type):
        return self._position.get_new_vte_rect(gtk_position_type)

    def _inform_expanded_rect(self, gtk_position_type):
        return self._position.get_expanded_rect(gtk_position_type)

    def _inform_shrinked_rect(self, gtk_position_type):
        return self._position.get_shrinked_rect(gtk_position_type)

    def _inform_can_shrink_to(self, gtk_position_type):
        return self._position.can_shrink_to(gtk_position_type)

    def _inform_container_itself(self):
        return self

    def adjust_position(self, gtk_position_type, rect):
        self._position.adjust(gtk_position_type, rect)

    def move_to(self, rect):
        self._position.move_to(rect)
