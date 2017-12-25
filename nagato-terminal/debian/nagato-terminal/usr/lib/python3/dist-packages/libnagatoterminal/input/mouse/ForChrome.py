from gi.repository import Gdk
from libnagato.Object import NagatoObject
from libnagatoterminal.menu.context.ForChrome import (
    NagatoForChrome as NagatoContextMenu
    )


class NagatoForChrome(NagatoObject):

    def _on_button_press(self, widget, event):
        yuki_x, yuki_y = self._widget.get_pointer()
        yuki_w, yuki_h = self._widget.get_size()
        if (yuki_w-16) > yuki_x > 16 and (yuki_h-16) > yuki_y > 16:
            return
        if event.button == 3:
            self._context_menu.pop_up()

    def __init__(self, parent, widget):
        self._parent = parent
        self._context_menu = NagatoContextMenu(self)
        self._widget = widget
        widget.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        widget.connect("button-press-event", self._on_button_press)
