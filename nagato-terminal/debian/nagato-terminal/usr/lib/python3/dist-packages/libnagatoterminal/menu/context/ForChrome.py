
from gi.repository import Gdk
from libnagatoterminal.menu.context.ContextCore import NagatoContextCore


class NagatoContextMenu(NagatoContextCore):

    def _on_button_press(self, widget, event):
        yuki_gdk_window, yuki_x, yuki_y = Gdk.Window.at_pointer()
        # widgets have any child, but containers not.
        if len(yuki_gdk_window.get_children()) > 0:
            self._on_right_click()
