
# NOTE for /proc/stat:
# 
# 0    1    2    3      4    5      6   7       8     9     10
# name user nice system idle iowait irq softirq steal guest guest_nice

class NagatoProcStat(object):

    def _set_data(self, data):
        yuki_index = 0
        for yuki_stat in data.strip().split(" "):
            if yuki_stat == "":
                continue
            if yuki_index == 0:
                self._name = yuki_stat
            if yuki_index in [4, 5]:
                self._idle += int(yuki_stat)
            if yuki_index in [9, 10]:
                self._non_idle -= int(yuki_stat)
            if yuki_index in [1, 2, 3, 6, 7, 8]:
                self._non_idle += int(yuki_stat)
            yuki_index += 1

    def __init__(self, data):
        self._idle = 0
        self._non_idle = 0
        self._set_data(data)

    @property
    def cpu_name(self):
        return self._name

    @property
    def total(self):
        return self._idle + self._non_idle

    @property
    def idle(self):
        return self._idle
