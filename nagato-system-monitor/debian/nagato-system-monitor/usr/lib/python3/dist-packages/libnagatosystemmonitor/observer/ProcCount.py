
import glob
from collections import deque

HISTORY_MAX = 200


class NagatoProcCount(object):

    def step(self):
        yuki_count = len(glob.glob("/proc/[0-9]*"))        
        self._current = yuki_count
        self._history.append(yuki_count)

    def __init__(self):
        self._current = 0
        self._history = deque(maxlen=HISTORY_MAX)

    @property
    def count(self):
        return self._current

    @property
    def proc_count_history(self):
        return self._history.copy()
