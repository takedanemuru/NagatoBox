

class NagatoObject(object):

    def _decode_message(self, message):
        message = message.replace("YUKI.N > ENQUIRY ", "_inform_")
        message = message.replace("YUKI.N > ", "_yuki_n_")
        message = message.replace(" ", "_")
        return message

    def _on_method_found(self, message, user_data=None):
        yuki_method = getattr(self, message)
        if user_data is not None:
            return yuki_method(user_data)
        else:
            return yuki_method()

    def _raise(self, message, user_data=None):
        if self._parent is not None:
            message = self._decode_message(message)
            return self._parent.N(message, user_data)
        else:
            return None

    def _enquiry(self, message, user_data=None):
        return self._raise(self, message, user_data)

    def N(self, message, user_data=None):
        if message in dir(self):
            return self._on_method_found(message, user_data)
        else:
            return self._raise(message, user_data)
