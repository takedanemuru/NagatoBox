
from collections import deque

HISTORY_MAX = 200


class NagatoMemInfo(object):

    def _set_momory_usage(self, usage):
        self._memory_usage = usage
        self._memory_history.append(usage) 

    def _set_swap_usage(self, usage):
        self._swap_usage = usage
        self._swap_history.append(usage) 

    def _read_lines(self, lines):
        for yuki_line in lines:
            if yuki_line.startswith("MemTotal:"):
                yuki_memory_total = int(yuki_line.split()[1])
            if yuki_line.startswith("MemAvailable:"):
                yuki_memory_available = int(yuki_line.split()[1])
            if yuki_line.startswith("SwapTotal:"):
                yuki_swap_total = int(yuki_line.split()[1])
            if yuki_line.startswith("SwapFree:"):
                yuki_swap_free = int(yuki_line.split()[1])
                break
        self._set_momory_usage(1-(yuki_memory_available/yuki_memory_total))
        self._set_swap_usage(1-(yuki_swap_free/yuki_swap_total))

    def step(self):
        with open("/proc/meminfo", "r") as lines:
            self._read_lines(lines)
        lines.close()

    def __init__(self):
        self._memory_usage = 0
        self._memory_history = deque(maxlen=HISTORY_MAX)
        self._swap_usage = 0
        self._swap_history = deque(maxlen=HISTORY_MAX)

    @property
    def memory_usage(self):
        return self._memory_usage

    @property
    def swap_usage(self):
        return self._swap_usage

    @property
    def memory_history(self):
        return self._memory_history.copy()

    @property
    def swap_history(self):
        return self._swap_history.copy()
