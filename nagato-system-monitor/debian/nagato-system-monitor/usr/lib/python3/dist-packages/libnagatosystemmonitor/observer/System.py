
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.observer.Stat import NagatoStat
from libnagatosystemmonitor.observer.MemInfo import NagatoMemInfo
from libnagatosystemmonitor.observer.ProcCount import NagatoProcCount
from libnagatosystemmonitor.observer.Thermal import NagatoThermal


class NagatoSystem(NagatoObject):

    def _get_histories_for_graph(self):
        return {
            "cpu": self._stat.cpu_history,
            "memory": self._mem_info.memory_history,
            "swap": self._mem_info.swap_history
            }

    def _get_data_for_label(self):
        return {
            "cpu": self._stat.cpu_usage,
            "memory": self._mem_info.memory_usage,
            "swap": self._mem_info.swap_usage,
            "count": self._proc_count.count,
            "temperature": self._thermal.temperature
            }

    def _raise_signals(self):
        self._raise("YUKI.N > step graph", self._get_histories_for_graph())
        self._raise("YUKI.N > step label", self._get_data_for_label())
        self._raise("YUKI.N > system step done", self._stat.cpu_time_diff)

    def observe(self):
        self._stat.step()
        self._mem_info.step()
        self._proc_count.step()
        self._thermal.step()
        self._raise_signals()

    def __init__(self, parent):
        self._parent = parent
        self._stat = NagatoStat()
        self._mem_info = NagatoMemInfo(self)
        self._proc_count = NagatoProcCount()
        self._thermal = NagatoThermal(self)
