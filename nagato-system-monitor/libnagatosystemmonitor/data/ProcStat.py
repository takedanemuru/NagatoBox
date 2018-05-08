
# NOTE for /proc/stat:
#
# 0    1    2    3      4    5      6   7       8     9     10
# name user nice system idle iowait irq softirq steal guest guest_nice

IDLE = (4, 5)
NON_IDLE = (1, 2, 3, 6, 7, 8)
NON_IDLE_GUEST = (9, 10)


class NagatoProcStat(object):

    def _get_total(self, data, indexes):
        yuki_total = 0
        for yuki_index in indexes:
            yuki_total += int(data[yuki_index])
        return yuki_total

    def __init__(self, data):
        yuki_data = data.strip().split()
        self._name = yuki_data[0]
        self._idle = self._get_total(yuki_data, IDLE)
        self._non_idle = self._get_total(yuki_data, NON_IDLE)
        self._non_idle_guest = self._get_total(yuki_data, NON_IDLE_GUEST)

    @property
    def cpu_name(self):
        return self._name

    @property
    def total(self):
        return self._idle + self._non_idle - self._non_idle_guest

    @property
    def idle(self):
        return self._idle
