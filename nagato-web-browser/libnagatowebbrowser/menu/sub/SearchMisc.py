
from libnagato.menu.Item import NagatoItem
from libnagatowebbrowser.menu.sub.SubCore import NagatoSubCore

MESSAGE = "YUKI.N > search selection"


class NagatoSearchMisc(NagatoSubCore):

    def _initialize_child_menus(self):
        NagatoItem(self, "debian source", MESSAGE,"!dsource")
        NagatoItem(self, "StackOverflow", MESSAGE,"!sof")

    def _set_variables(self):
        self._title = "Misc"
