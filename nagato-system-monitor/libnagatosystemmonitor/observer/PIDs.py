
import glob
from collections import deque


class NagatoPIDs(object):

    def _get_usage(self, pid, current_total):
        if pid in self._time_total_per_pids:
            yuki_diff = current_total-self._time_total_per_pids[pid]
            yuki_usage = yuki_diff/self._cpu_time_diff
        else:
            yuki_usage = 0
        self._time_total_per_pids[pid] = current_total
        return yuki_usage

    def _read_data(self, directory):
        yuki_process = {}
        try:
            with open(directory+"/stat", "r") as yuki_line:
                yuki_data = yuki_line.read().split()
                yuki_pid = yuki_data[0]
                yuki_process["pid"] = int(yuki_pid)
                yuki_process["ppid"] = int(yuki_data[3])
                yuki_process["name"] = yuki_data[1]
                yuki_process["vsize"] = float(yuki_data[22])
                yuki_process["rss"] = float(yuki_data[23])
                yuki_total = int(yuki_data[13])+int(yuki_data[14])
                yuki_usage = self._get_usage(yuki_pid, yuki_total)
                yuki_process["usage"] = yuki_usage
        except FileNotFoundError:
            return
        yuki_line.close()
        if yuki_usage > 0:
            self._processes.append(yuki_process)

    def observe(self, cpu_time_diff):
        self._processes.clear()
        self._cpu_time_diff = max(1,cpu_time_diff)
        for yuki_path in glob.glob("/proc/[0-9]*"):
            self._read_data(yuki_path)

    def __init__(self):
        self._processes = deque()
        self._cpu_time_diff = 1
        self._time_total_per_pids = {}

    @property
    def active_processes(self):
        return self._processes
