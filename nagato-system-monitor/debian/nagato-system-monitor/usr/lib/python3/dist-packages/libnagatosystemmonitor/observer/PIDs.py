
import glob
from collections import deque
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.reader.ProcID import NagatoProcID


class NagatoPIDs(NagatoObject):

    def _yuki_n_process_data(self, process_data):
        self._processes.append(process_data)

    def observe(self, cpu_time_diff):
        self._processes.clear()
        for yuki_path in glob.glob("/proc/[0-9]*"):
            self._reader.read(yuki_path, cpu_time_diff)

    def __init__(self):
        self._parent = None
        self._processes = deque()
        self._reader = NagatoProcID(self)

    @property
    def active_processes(self):
        return self._processes
