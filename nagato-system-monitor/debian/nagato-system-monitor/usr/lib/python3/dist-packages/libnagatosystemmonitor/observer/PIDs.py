
import glob
from collections import deque
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.reader.ProcID import NagatoProcID
from libnagatosystemmonitor.observer.PidBlockers import NagatoPidBlockers


class NagatoPIDs(NagatoObject):

    def _yuki_n_process_data(self, process_data):
        for yuki_key in ("rss", "usage"):
            if process_data[yuki_key] == 0 and self._blockers[yuki_key]:
                return
        self._processes.append(process_data)

    def observe(self, cpu_time_diff):
        self._processes.clear()
        for yuki_path in glob.glob("/proc/[0-9]*"):
            self._reader.read(yuki_path, cpu_time_diff)
        self._raise("YUKI.N > step cell", self._processes)

    def __init__(self, parent):
        self._parent = parent
        self._processes = deque()
        self._blockers = NagatoPidBlockers(self)
        self._reader = NagatoProcID(self)
