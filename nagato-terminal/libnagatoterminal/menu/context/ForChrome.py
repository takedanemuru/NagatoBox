
from libnagatoterminal.menu.context.ContextCore import NagatoContextCore

class NagatoForChrome(NagatoContextCore):

    def _is_mouse_on_chrome(self):
        yuki_x, yuki_y = self._parent.get_pointer()
        yuki_w, yuki_h = self._parent.get_size()
        if (yuki_w-16) > yuki_x > 16 and (yuki_h-16) > yuki_y > 16:
            return False
        return True

    def _on_button_press(self, widget, event):
        if self._is_mouse_on_chrome() and event.button == 3:
            self._on_right_click()
