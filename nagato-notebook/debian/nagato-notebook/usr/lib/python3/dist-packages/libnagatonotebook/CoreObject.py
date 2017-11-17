

class NagatoObject(object):

    def _initialize_ext(self, user_data):
        pass

    def _decode(self, message):
        message = message.replace("YUKI.N > ", "_yuki_n_")
        message = message.replace(" ", "_")
        return message

    def _raise(self, message, user_data=None):
        if self._parent is not None:
            self._parent.N(self._decode(message), user_data)

    def _catch(self, message, user_data=None):
        yuki_method = getattr(self, message)
        if user_data is not None:
            yuki_method(user_data)
        else:
            yuki_method()

    def N(self, message, user_data=None):
        if message in dir(self):
            self._catch(message, user_data)
        else:
            self._raise(message, user_data)
