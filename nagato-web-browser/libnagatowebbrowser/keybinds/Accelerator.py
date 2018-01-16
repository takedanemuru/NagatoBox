
from libnagato.Object import NagatoObject


class NagatoAccelerator(NagatoObject):

    def _matches(self, event_state):
        if self._mask is None:
            return True
        if (self._mask & event_state == self._mask):
            return True
        return False

    def _get_value(self, keyval_name):
        if (keyval_name in self._binds[keyval_name]):
            return self._binds[keyval_name]
        return None

    def __call__(self, event_state, keyval_name):
        if not (keyval_name in self._binds):
            return False
        if not self._matches(event_state):
            return False
        self._raise(self._binds[keyval_name], self._get_value(keyval_name))
        return True 

    def __init__(self, parent, mask, binds, values):
        self._parent = parent
        self._mask = mask
        self._binds = binds
        self._values = values
