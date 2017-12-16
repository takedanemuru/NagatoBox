

class NagatoObject(object):

    def _decode(self, message, header):
        message = message.replace("YUKI.N > ", header)
        message = message.replace(" ", "_")
        return message

    def _enquiry(self, message, user_data=None):
        if self._parent is not None:
            return self._parent.N(self._decode(message, "_inform_"), user_data)

    def _raise(self, message, user_data=None):
        if self._parent is not None:
            self._parent.N(self._decode(message, "_yuki_n_"), user_data)

    def _catch(self, message, user_data=None):
        yuki_method = getattr(self, message)
        if user_data is not None:
            return yuki_method(user_data)
        else:
            return yuki_method()

    def _bridge(self, message, user_data=None):
        if self._parent is not None:
            return self._parent.N(message, user_data)

    def N(self, message, user_data=None):
        if message in dir(self):
            return self._catch(message, user_data)
        else:
            return self._bridge(message, user_data)
