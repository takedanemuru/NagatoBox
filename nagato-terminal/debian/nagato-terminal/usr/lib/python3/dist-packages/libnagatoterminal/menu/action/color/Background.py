
from libnagatoterminal.menu.action.color.Color import NagatoColor


class NagatoBackground(NagatoColor):

    def _initialize_variables(self):
        self._title = "Select Background Color"
        self._query = "vte", "background_color"
        self._message = "YUKI.N > config"
