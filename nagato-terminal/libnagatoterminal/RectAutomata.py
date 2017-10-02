
from libnagatoterminal.Rect import NagatoRect


class NagatoRectAutomata(object):

    def _get_offset_rect(self, left, top, width, height):
        yuki_rect = NagatoRect(
            self._rect._left + left,
            self._rect._top + top,
            self._rect._width + width,
            self._rect._height + height,
            )
        return yuki_rect

    def __init__(self, rect):
        self._rect = rect
