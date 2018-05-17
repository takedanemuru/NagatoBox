
from gi.repository import Gdk
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Context import NagatoContextCore
from libnagato.menu.Separator import NagatoSeparator
from libnagato.menu.SelectBackgroundImage import NagatoSelectBackgroundImage


class NagatoContextMenu(NagatoContextCore):

    def _on_button_press(self, widget, event):
        yuki_gdk_window, yuki_x, yuki_y = Gdk.Window.at_pointer()
        if len(yuki_gdk_window.get_children()) > 0:
            self._on_right_click()

    def _initialize_children(self):
        NagatoSelectBackgroundImage(self)
        NagatoSeparator(self)
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")
