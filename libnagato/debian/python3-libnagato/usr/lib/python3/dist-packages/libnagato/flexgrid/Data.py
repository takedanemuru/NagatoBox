

class NagatoData(object):

    def __init__(self, signal_from, direction, destination_rect):
        self._signal_from = signal_from
        self._direction = direction
        self._destionation_rect = destination_rect

    @property
    def signal_from(self):
        return self._signal_from

    @property
    def direction(self):
        return self._direction

    @property
    def destination_rect(self):
        return self._destionation_rect
