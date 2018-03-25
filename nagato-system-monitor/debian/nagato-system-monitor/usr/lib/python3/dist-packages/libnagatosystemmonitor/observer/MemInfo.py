
from libnagatosystemmonitor.data.History import NagatoHistory

HISTORY_MAX = 200


class NagatoMemInfo(object):

    def _read_line(self, line):
        if line.startswith("MemTotal:"):
            self._memory.set_total(int(line.split()[1]))
        if line.startswith("MemAvailable:"):
            self._memory.set_free(int(line.split()[1]))
        if line.startswith("SwapTotal:"):
            self._swap.set_total(int(line.split()[1]))
        if line.startswith("SwapFree:"):
            self._swap.set_free(int(line.split()[1]))
            return True
        return False

    def _read_lines(self, lines):
        for yuki_line in lines:
            if self._read_line(yuki_line):
                break

    def step(self):
        with open("/proc/meminfo", "r") as lines:
            self._read_lines(lines)
            lines.close()

    def __init__(self):
        self._memory = NagatoHistory(HISTORY_MAX)
        self._swap = NagatoHistory(HISTORY_MAX)

    @property
    def memory_usage(self):
        return self._memory.current

    @property
    def swap_usage(self):
        return self._swap.current

    @property
    def memory_history(self):
        return self._memory.history

    @property
    def swap_history(self):
        return self._swap.history
