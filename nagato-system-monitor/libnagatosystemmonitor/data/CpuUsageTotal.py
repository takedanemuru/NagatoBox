
from libnagatosystemmonitor.data.ProcStat import NagatoProcStat


class NagatoCpuUsageTotal(object):

    def _get_current_usage(self, proc_stat):
        self._total_diff = proc_stat.total-self._prev_proc_stat.total
        yuki_idle = proc_stat.idle-self._prev_proc_stat.idle
        return (self._total_diff-yuki_idle)/self._total_diff

    def get_usage(self, data):
        yuki_proc_stat = NagatoProcStat(data)
        if self._prev_proc_stat is None:
            yuki_usage = 0
        if self._prev_proc_stat is not None:
            yuki_usage = self._get_current_usage(yuki_proc_stat)
        self._prev_proc_stat = yuki_proc_stat
        return yuki_usage

    def __init__(self):
        self._prev_proc_stat = None
        self._total_diff = 0

    @property
    def time_diff(self):
        return self._total_diff
