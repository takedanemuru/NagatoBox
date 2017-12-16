
from gi.repository import Gtk
from libnagatowebbrowser.CoreObject import NagatoObject
from libnagatowebbrowser.menu.Item import NagatoItem
from libnagatowebbrowser.menu.Separator import NagatoSeparator


class NagatoCore(NagatoObject):

    def _add_menu_item(self, title, message):
        yuki_item = NagatoItem(
            self,
            title,
            message,
            None,
            self._root_menu)
        self._menus.append(yuki_item)

    def _add_separator(self):
        yuki_separator = NagatoSeparator(self._root_menu)
        self._menus.append(yuki_separator)

    def _hide_all(self):
        for yuki_menu in self._menus:
            yuki_menu.hide()

    def _on_toggle_hide(self, hit_test_result):
        pass

    def _add_menu_items(self):
        pass

    def toggle(self, hit_test_result):
        self._on_toggle_hide(hit_test_result)

    def __init__(self, parent):
        self._menus = []
        self._parent = parent
        self._root_menu = parent
        self._add_menu_items()
        self._add_separator()
