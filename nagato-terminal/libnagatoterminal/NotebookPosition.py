
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.automata.rect.Adjust import NagatoAdjust
from libnagatoterminal.automata.rect.Expand import NagatoExpand
from libnagatoterminal.automata.rect.Shrink import NagatoShrink
from libnagatoterminal.automata.rect.New import NagatoNew


class NagatoNotebookPosition(NagatoRect):

    def __init__(self, left, top, width=1, height=1):
        NagatoRect.__init__(self, left, top, width, height)
        self._automata_adjust = NagatoAdjust(self)
        self._automata_expand = NagatoExpand(self)
        self._automata_shrink = NagatoShrink(self)
        self._automata_new = NagatoNew(self)

    def adjust(self, gtk_position_type, rect):
        self._automata_adjust.adjust(gtk_position_type, rect)

    def get_new_vte_rect(self, gtk_position_type):
        return self._automata_new(gtk_position_type)

    def get_expanded_rect(self, gtk_position_type):
        return self._automata_expand(gtk_position_type)

    def get_shrinked_rect(self, gtk_position_type):
        return self._automata_shrink(gtk_position_type)

    def can_shrink_to(self, gtk_position_type):
        return self._automata_shrink.can_shrink_to(gtk_position_type)
