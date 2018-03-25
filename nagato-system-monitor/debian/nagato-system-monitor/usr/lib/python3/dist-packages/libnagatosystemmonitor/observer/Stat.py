
from collections import deque
from libnagatosystemmonitor.data.ProcStat import NagatoProcStat

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
        self._current = yuki_usage
        self._stat_history.append(yuki_usage)
        self._prev_proc_stat = proc_stat

    def _read_lines(self, lines):
        for yuki_line in lines:
            if not yuki_line.startswith("cpu "):
                break
            self._set_data(NagatoProcStat(yuki_line))

    def step(self):
        with open("/proc/stat", "r") as lines:
            self._read_lines(lines)
        lines.close()

    def __init__(self):
        self._stat_history = deque(maxlen=HISTORY_MAX)
        self._prev_proc_stat = None
        self._current = 0
        self._total_diff = 0

    @property
    def cpu_usage(self):
        return self._current

    @property
    def cpu_history(self):
        return self._stat_history.copy()

    @property
    def cpu_time_diff(self):
        return self._total_diff
