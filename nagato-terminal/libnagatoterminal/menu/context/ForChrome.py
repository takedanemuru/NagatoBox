
from gi.repository import Gdk
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator
from libnagatoterminal.menu.context.ContextCore import NagatoContextCore
from libnagatoterminal.menu.item.action.BackgroundImage import (
    NagatoBackgroundImage)


class NagatoContextMenu(NagatoContextCore):

    def _initialize_children(self):
        NagatoBackgroundImage(self)
        NagatoSeparator(self)
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")

    def _on_button_press(self, widget, event):
        yuki_gdk_window, yuki_x, yuki_y = Gdk.Window.at_pointer()
        # widgets have any child, but containers not.
        if len(yuki_gdk_window.get_children()) > 0:
            self._on_right_click()
