
from gi.repository import Gdk
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Context import NagatoContextCore
from libnagato.menu.Separator import NagatoSeparator
from libnagatotext.menu.action.BackgroundImage import NagatoBackgroundImage


class NagatoContextMenu(NagatoContextCore):

    def _on_button_press(self, widget, event):
        yuki_gdk_window, yuki_x, yuki_y = Gdk.Window.at_pointer()
        # widgets have no children, but containers not.
        if yuki_gdk_window is None:
            return
        if len(yuki_gdk_window.get_children()) > 0:
            self._on_right_click()

    def _initialize_children(self):
        NagatoBackgroundImage(self)
        NagatoSeparator(self)
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")
