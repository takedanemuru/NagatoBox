

class NagatoObject(object):

    def _decode(self, message, header):
        message = message.replace("YUKI.N > ", header)
        return message.replace(" ", "_")

    def _on_method_found(self, message, user_data=None):
        yuki_method = getattr(self, message)
        if user_data is not None:
            return yuki_method(user_data)
        else:
            return yuki_method()

    def _inform_itself(self, class_name):
        print("CAUTION: this method is for testing only")
        if class_name == __class__.__name__:
            return self
        else:
            return self._enquiry("YUKI.N > itself", class_name)

    def _enquiry(self, message, user_data=None):
        if self._parent is not None:
            message = self._decode(message, "_inform_")
            return self._parent.data_connect(message, user_data)

    def _raise(self, message, user_data=None):
        if self._parent is not None:
            message = self._decode(message, "_yuki_n_")
            return self._parent.data_connect(message, user_data)

    def _bridge(self, message, user_data=None):
        if self._parent is not None:
            return self._parent.data_connect(message, user_data)

    def data_connect(self, message, user_data=None):
        if message in dir(self):
            return self._on_method_found(message, user_data)
        else:
            return self._bridge(message, user_data)
