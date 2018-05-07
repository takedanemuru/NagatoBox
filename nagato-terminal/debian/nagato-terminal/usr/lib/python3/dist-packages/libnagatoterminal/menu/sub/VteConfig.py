
from libnagatoterminal.menu.sub.SubCore import NagatoSubCore
from libnagatoterminal.menu.action.Font import NagatoFont
from libnagatoterminal.menu.action.color.Foreground import NagatoForeground
from libnagatoterminal.menu.action.color.Background import NagatoBackground
from libnagatoterminal.menu.sub.Opacity import NagatoOpacity


class NagatoVteConfig(NagatoSubCore):

    def _initialize_child_menus(self):
        NagatoFont(self)
        NagatoForeground(self)
        NagatoBackground(self)
        NagatoOpacity(self)

    def _set_variables(self):
        self._title = "Config"
        self._data_query = ""
