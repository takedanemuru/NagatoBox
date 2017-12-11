

class NagatoUnnullableArray(object):

    def __init__(self):
        self._internal_array = []

    def append(self, data):
        if data is not None:
            self._internal_array.append(data)

    @property
    def data(self):
        return self._internal_array
