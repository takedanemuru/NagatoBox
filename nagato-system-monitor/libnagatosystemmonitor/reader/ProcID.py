
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.data.CpuUsage import NagatoCpuUsage
from libnagatosystemmonitor.Mikuru import Process


class NagatoProcID(NagatoObject):

    def _construct_process_data(self, data):
        yuki_pid = int(data[0])
        yuki_usage = self._cpu_usage.get(yuki_pid, data)
        yuki_process = {}
        yuki_process["pid"] = yuki_pid
        yuki_process["ppid"] = int(data[3])
        yuki_process["usage"] = yuki_usage
        yuki_process["vsize"] = float(data[22])/1024/1024
        yuki_process["rss"] = float(data[23])/256
        yuki_process["comm"] = Process.get_command(yuki_pid)
        self._raise("YUKI.N > process data", yuki_process)

    def read(self, directory, cpu_time_diff):
        try:
            with open(directory+"/stat", "r") as yuki_line:
                yuki_data = yuki_line.read().split()
                yuki_line.close()
        except FileNotFoundError:
            return
        self._cpu_usage.set_cpu_time_diff(cpu_time_diff)
        self._construct_process_data(yuki_data)

    def __init__(self, parent):
        self._parent = parent
        self._cpu_usage = NagatoCpuUsage()
