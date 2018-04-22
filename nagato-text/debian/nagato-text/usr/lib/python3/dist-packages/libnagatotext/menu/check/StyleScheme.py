from libnagatotext.menu.check.Check import NagatoCheck


class NagatoStyleScheme(NagatoCheck):

    def _on_activate(self):
        self._raise("YUKI.N > scheme", self._title)
        yuki_data = "sourceview", "style_scheme", self._title
        self._raise(self._message, yuki_data)

    def _on_map(self, widget):
        yuki_active = (self._enquiry(self._query, self._data) == self._title)
        self._set_active_without_signal(yuki_active)

    def _initialize_variables(self, user_data=None):
        self._title = user_data
        self._query = "YUKI.N > config"
        self._data = "sourceview", "style_scheme"
        self._message = "YUKI.N > config"
