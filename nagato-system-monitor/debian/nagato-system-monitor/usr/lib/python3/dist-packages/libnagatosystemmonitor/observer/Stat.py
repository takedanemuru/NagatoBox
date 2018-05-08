
from collections import deque
from libnagatosystemmonitor.data.ProcStat import NagatoProcStat
from pathlib import Path

HISTORY_MAX = 200


class NagatoStat(object):

    def _get_current_usage(self, proc_stat):
        self._total_diff = proc_stat.total-self._prev_proc_stat.total
        yuki_idle = proc_stat.idle-self._prev_proc_stat.idle
        return (self._total_diff-yuki_idle)/self._total_diff

    def _set_data(self, proc_stat):
        if self._prev_proc_stat is None:
            yuki_usage = 0
        if self._prev_proc_stat is not None:
            yuki_usage = self._get_current_usage(proc_stat)
        self._prev_proc_stat = proc_stat
        self._stat_history.append(yuki_usage)

    def _read_lines(self, lines):
        for yuki_line in lines:
            if not yuki_line.startswith("cpu "):
                break
            self._set_data(NagatoProcStat(yuki_line))

    def step(self):
        with Path("/proc/stat").open() as yuki_lines:
            self._read_lines(yuki_lines)

    def __init__(self):
        self._stat_history = deque(maxlen=HISTORY_MAX)
        self._prev_proc_stat = None
        self._total_diff = 0

    @property
    def cpu_usage(self):
        return self._stat_history[-1]

    @property
    def cpu_history(self):
        return self._stat_history.copy()

    @property
    def cpu_time_diff(self):
        return self._total_diff
