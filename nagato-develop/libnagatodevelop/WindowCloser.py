
from libnagatodevelop.dialog.WarningQuit import NagatoWarningQuit


class NagatoWindowCloser(object):

    def set_force_close(self):
        self._force_close = True

    def can_close(self):
        if self._force_close:
            self._force_close = False
            return True
        return NagatoWarningQuit.call()

    def __init__(self):
        self._force_close = False
