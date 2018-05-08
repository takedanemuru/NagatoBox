
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.data.History import NagatoHistory
from libnagatosystemmonitor.reader.ProcMeminfo import NagatoProcMeminfo

HISTORY_MAX = 200


class NagatoMemInfo(NagatoObject):

    def _yuki_n_memory_total(self, data):
        self._memory.set_total(data)

    def _yuki_n_memory_free(self, data):
        self._memory.set_free(data)

    def _yuki_n_swap_total(self, data):
        self._swap.set_total(data)

    def _yuki_n_swap_free(self, data):
        self._swap.set_free(data)

    def step(self):
        self._reader.read()

    def __init__(self, parent):
        self._parent = parent
        self._reader = NagatoProcMeminfo(self)
        self._memory = NagatoHistory(HISTORY_MAX)
        self._swap = NagatoHistory(HISTORY_MAX)

    @property
    def memory_usage(self):
        return self._memory.current

    @property
    def swap_usage(self):
        return self._swap.current

    @property
    def memory_history(self):
        return self._memory.history

    @property
    def swap_history(self):
        return self._swap.history
