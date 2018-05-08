
from pathlib import Path
from libnagato.Object import NagatoObject

MESSAGES = {
    "MemTotal:": "YUKI.N > memory total",
    "MemAvailable:": "YUKI.N > memory free",
    "SwapTotal:": "YUKI.N > swap total",
    "SwapFree:": "YUKI.N > swap free"
    }


class NagatoProcMeminfo(NagatoObject):

    def _read_line(self, line):
        yuki_header = line.split()[0]
        if yuki_header in MESSAGES:
            self._raise(MESSAGES[yuki_header], int(line.split()[1]))
        if yuki_header == "SwapFree:":
            return True

    def _read_lines(self, lines):
        for yuki_line in lines:
            if self._read_line(yuki_line):
                break

    def read(self):
        with Path("/proc/meminfo").open() as yuki_lines:
            self._read_lines(yuki_lines)

    def __init__(self, parent):
        self._parent = parent
