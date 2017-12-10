
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.RectAutomataAdjust import NagatoRectAutomataAdjust
from libnagatoterminal.RectAutomataExpand import NagatoRectAutomataExpand
from libnagatoterminal.RectAutomataShrink import NagatoRectAutomataShrink
from libnagatoterminal.RectAutomataNew import NagatoRectAutomataNew

class NagatoNotebookPosition(NagatoRect):

    def __init__(self, left, top, width=1, height=1):
        NagatoRect.__init__(self, left, top, width, height)
        self._automata_adjust = NagatoRectAutomataAdjust(self)
        self._automata_expand = NagatoRectAutomataExpand(self)
        self._automata_shrink = NagatoRectAutomataShrink(self)
        self._automata_new = NagatoRectAutomataNew(self)

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
