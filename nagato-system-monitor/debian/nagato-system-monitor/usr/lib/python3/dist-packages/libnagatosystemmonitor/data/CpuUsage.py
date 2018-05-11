

class NagatoCpuUsage(object):

    def _get_usage(self, pid, current_total):
        if pid in self._time_total_per_pids:
            yuki_diff = current_total-self._time_total_per_pids[pid]
            yuki_usage = yuki_diff/self._cpu_time_diff
        else:
            yuki_usage = 0
        self._time_total_per_pids[pid] = current_total
        return yuki_usage

    def get(self, pid, data):
        yuki_total = int(data[13])+int(data[14])
        yuki_usage = self._get_usage(pid, yuki_total)
        return yuki_usage

    def set_cpu_time_diff(self, cpu_time_diff):
        self._cpu_time_diff = max(1, cpu_time_diff)

    def __init__(self):
        self._cpu_time_diff = 1
        self._time_total_per_pids = {}
