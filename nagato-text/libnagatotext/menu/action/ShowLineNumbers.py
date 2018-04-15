
from libnagatotext.menu.check.Check import NagatoCheck


class NagatoShowLineNumbers(NagatoCheck):

    def _on_activate(self):
        yuki_current = self._enquiry(self._query, self._data)
        yuki_new = "yes" if yuki_current == "no" else "no"
        yuki_data = "sourceview", "show_line_numbers", yuki_new
        self._raise(self._message, yuki_data)

    def _on_map(self, widget):
        yuki_active = (self._enquiry(self._query, self._data) == "yes")
        self._set_active_without_signal(yuki_active)

    def _initialize_variables(self, user_data=None):
        self._title = "Show Line Numbers"
        self._query = "YUKI.N > config"
        self._data = "sourceview", "show_line_numbers"
        self._message = "YUKI.N > config"
