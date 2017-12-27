

class NagatoRect(object):

    def move_to(self, rect):
        self._top = rect.top
        self._left = rect.left
        self._height = rect.height
        self._width = rect.width

    def __init__(self, left, top, width=1, height=1):
        self._left = left
        self._top = top
        self._width = width
        self._height = height

    @property
    def left(self):
        return self._left

    @property
    def top(self):
        return self._top

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def right(self):
        return (self._left+self._width-1)

    @property
    def bottom(self):
        return (self._top+self._height-1)
