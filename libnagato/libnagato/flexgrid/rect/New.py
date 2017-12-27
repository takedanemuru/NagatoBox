
from libnagato.datatype.Rect import NagatoRect
from libnagato.flexgrid.rect.Core import NagatoCore


class NagatoNew(NagatoCore):

    def _get_right(self):
        return NagatoRect(self._rect.right+1, self._rect._top)

    def _get_bottom(self):
        return NagatoRect(self._rect._left, self._rect.bottom+1)

    def _get_top(self):
        return NagatoRect(self._rect._left, self._rect._top-1)

    def _get_left(self):
        return NagatoRect(self._rect._left-1, self._rect._top)
