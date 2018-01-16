
from libnagato.menu.Item import NagatoItem
from libnagatowebbrowser.menu.sub.SubCore import NagatoSubCore

MESSAGE = "YUKI.N > search selection"


class NagatoSearchWeb(NagatoSubCore):

    def _initialize_child_menus(self):
        NagatoItem(self, "DuckDuckGo", MESSAGE, "!safe")
        NagatoItem(self, "Google", MESSAGE, "!g")
        NagatoItem(self, "Bing", MESSAGE, "!bing")
        NagatoItem(self, "Yandex", MESSAGE, "!yandex")

    def _set_variables(self):
        self._title = "Web"
