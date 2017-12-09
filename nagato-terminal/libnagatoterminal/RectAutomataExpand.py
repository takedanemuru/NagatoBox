
from libnagatoterminal.Rect import NagatoRect
from libnagatoterminal.RectAutomata import NagatoRectAutomata


class NagatoRectAutomataExpand(NagatoRectAutomata):

    def _get_right(self):
        return self._get_offset_rect(0, 0, 1, 0)

    def _get_bottom(self):
        return self._get_offset_rect(0, 0, 0, 1)

    def _get_top(self):
        return self._get_offset_rect(0, -1, 0, 1)

    def _get_left(self):
        return self._get_offset_rect(-1, 0, 1, 0)
