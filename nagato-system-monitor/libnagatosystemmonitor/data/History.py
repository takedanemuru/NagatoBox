
from collections import deque


class NagatoHistory(object):

    def set_total(self, total):
        self._total_buffer = total

    def set_free(self, free):
        yuki_usage = 1-(free/self._total_buffer)
        self._current = yuki_usage
        self._history.append(yuki_usage)

    def __init__(self, max_length):
        self._current = 0
        self._history = deque(maxlen=max_length)
        self._total_buffer = 0

    @property
    def current(self):
        return self._current

    @property
    def history(self):
        return self._history.copy()
