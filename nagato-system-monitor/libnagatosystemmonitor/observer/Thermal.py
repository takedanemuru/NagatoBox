
from pathlib import Path
from libnagato.Object import NagatoObject

PATH = "/sys/class/thermal/thermal_zone0/temp"


class NagatoThermal(NagatoObject):

    def step(self):
        yuki_thermal = self._path.read_text().replace("\n", "")
        self._temperature = (float(yuki_thermal)/1000)

    def __init__(self, parent):
        self._parent = parent
        self._path = Path(PATH)

    @property
    def temperature(self):
        return self._temperature
