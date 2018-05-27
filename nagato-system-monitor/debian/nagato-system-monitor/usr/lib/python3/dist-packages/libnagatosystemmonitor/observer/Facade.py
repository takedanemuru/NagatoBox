
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.observer.System import NagatoSystem
from libnagatosystemmonitor.observer.PIDs import NagatoPIDs


class NagatoFacade(NagatoObject):

    def _yuki_n_system_step_done(self, cpu_time_diff):
        self._pids.observe(cpu_time_diff)

    def step(self, index=None):
        self._system.observe()

    def __init__(self, parent):
        self._parent = parent
        self._system = NagatoSystem(self)
        self._pids = NagatoPIDs(self)
