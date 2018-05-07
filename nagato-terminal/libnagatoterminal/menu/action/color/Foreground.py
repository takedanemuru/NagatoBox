
from libnagatoterminal.menu.action.color.Color import NagatoColor


class NagatoForeground(NagatoColor):

    def _initialize_variables(self):
        self._title = "Select Foreground Color"
        self._query = "vte", "foreground_color"
        self._message = "YUKI.N > config"
