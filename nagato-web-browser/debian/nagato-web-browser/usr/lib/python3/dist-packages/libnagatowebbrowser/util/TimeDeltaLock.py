

from datetime import datetime

class NagatoTimeDeltaLock(object):

    def check_diff(self, diff):
        yuki_last_time = datetime.now()
        yuki_time_delta = yuki_last_time - self._last_time
        self._last_time = yuki_last_time
        return (yuki_time_delta.total_seconds() >= diff)

    def __init__(self):
        self._last_time = datetime.now()
