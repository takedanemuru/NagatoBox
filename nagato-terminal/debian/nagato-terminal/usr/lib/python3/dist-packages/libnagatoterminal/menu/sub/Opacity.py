
from libnagatoterminal.menu.sub.SubCore import NagatoSubCore
from libnagato.menu.Item import NagatoItem


class NagatoOpacity(NagatoSubCore):

    def _initialize_child_menus(self):
        for yuki_opacity in range(100, 0, -5):
            yuki_data = "css", "opacity", str(yuki_opacity/100)
            NagatoItem(self, yuki_opacity, "YUKI.N > config", yuki_data)

    def _set_variables(self):
        self._title = "Opacity (%)"
        self._data_query = ""
