
from libnagato.Object import NagatoObject


class NagatoPrime(NagatoObject):

    def _dispatch(self, header, message, user_data):
        yuki_message = self._decode(message, header)
        if yuki_message in dir(self):
            self.data_connect(yuki_message, user_data)

    def prime_call(self, message, user_data=None):
        if "_prime_object" in dir(self):
            self._prime_object.prime_call(message, user_data)
        else:
            self._dispatch("_yuki_n_", message, user_data)
