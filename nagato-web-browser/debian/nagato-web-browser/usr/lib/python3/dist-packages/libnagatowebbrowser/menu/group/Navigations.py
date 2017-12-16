
from libnagatowebbrowser.menu.group.Core import NagatoCore
from libnagatowebbrowser.menu.item.sensitive.GoBack import NagatoGoBack
from libnagatowebbrowser.menu.item.sensitive.GoForward import NagatoGoForward
from libnagatowebbrowser.menu.item.sensitive.StopLoading import (
    NagatoStopLoading
    )


class NagatoNavigations(NagatoCore):

    def _add_menu_items(self):
        self._menus.append(NagatoGoBack(self,self._root_menu))
        self._menus.append(NagatoGoForward(self,self._root_menu))
        self._add_menu_item("Reload", "YUKI.N > reload")
        self._menus.append(NagatoStopLoading(self,self._root_menu))
