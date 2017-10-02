
from libnagatoterminal.Vte import NagatoVte
from libnagatoterminal.GridPosition import NagatoGridPosition


class NagatoVteExtGridPosition(NagatoVte):

    def _initialize_ext(self, user_data):
        self._position = NagatoGridPosition(user_data.left, user_data.top)

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

    def adjust_position(self, gtk_position_type, rect):
        self._position.adjust(gtk_position_type, rect)

    def move_to(self, rect):
        self._position.move_to(rect)

    @property
    def left(self):
        return self._position.left

    @property
    def top(self):
        return self._position.top
