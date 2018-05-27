
from collections import deque
from libnagatosystemmonitor.data.ProcStat import NagatoProcStat
from libnagatosystemmonitor.data.CpuUsageTotal import NagatoCpuUsageTotal
from pathlib import Path

HISTORY_MAX = 200


class NagatoStat(object):

    def _read_lines(self, lines):
        for yuki_line in lines:
            if not yuki_line.startswith("cpu "):
                break
            yuki_usage = self._cpu_usage.get_usage(yuki_line)
            self._stat_history.append(yuki_usage)

    def step(self):
        with Path("/proc/stat").open() as yuki_lines:
            self._read_lines(yuki_lines)

    def __init__(self):
        self._stat_history = deque(maxlen=HISTORY_MAX)
        self._cpu_usage = NagatoCpuUsageTotal()

    @property
    def cpu_usage(self):
        return self._stat_history[-1]

    @property
    def cpu_history(self):
        return self._stat_history.copy()

    @property
    def cpu_time_diff(self):
        return self._cpu_usage.time_diff
