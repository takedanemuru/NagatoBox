
import threading
import time
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.observer.Stat import NagatoStat
from libnagatosystemmonitor.observer.MemInfo import NagatoMemInfo
from libnagatosystemmonitor.observer.ProcCount import NagatoProcCount
from libnagatosystemmonitor.observer.PIDs import NagatoPIDs

INTERVAL = 2


class NagatoThread(NagatoObject):

    def _get_histories_for_graph(self):
        yuki_histories_for_graph = {
            "cpu": self._stat.cpu_history,
            "memory": self._mem_info.memory_history,
            "swap": self._mem_info.swap_history
            }
        return yuki_histories_for_graph

    def _get_data_for_label(self):
        yuki_data_for_label = {
            "cpu": self._stat.cpu_usage,
            "memory": self._mem_info.memory_usage,
            "swap": self._mem_info.swap_usage,
            "count": self._proc_count.count
            }
        return yuki_data_for_label

    def _idle(self, index):
        self._stat.step()
        self._mem_info.step()
        self._proc_count.step()
        self._pids.observe(self._stat.cpu_time_diff)
        self._raise("YUKI.N > step graph", self._get_histories_for_graph())
        self._raise("YUKI.N > step label", self._get_data_for_label())
        self._raise("YUKI.N > step cell", self._pids.active_processes)

    def _target(self):
        while self._enabled:
            GLib.idle_add(self._idle, None, priority=GLib.PRIORITY_LOW)
            time.sleep(INTERVAL)
        self._raise("YUKI.N > stopped")

    def stop(self):
        self._enabled = False

    def start(self):
        self._enabled = True
        self._thread.start()

    def __getitem__(self, key):
        return None

    def __init__(self, parent):
        self._parent = parent
        self._stat = NagatoStat()
        self._mem_info = NagatoMemInfo()
        self._proc_count = NagatoProcCount()
        self._pids = NagatoPIDs()
        self._enabled = False
        self._thread = threading.Thread(target=self._target)
        self._thread.daemon = True
