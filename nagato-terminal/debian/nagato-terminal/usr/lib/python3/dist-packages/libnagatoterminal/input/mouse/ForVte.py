from gi.repository import Gdk
from libnagato.Object import NagatoObject
from libnagatoterminal.menu.context.ForVte import (
    NagatoForVte as NagatoContextMenu
    )


class NagatoForVte(NagatoObject):

    def _on_button_press(self, widget, event):
        if event.button == 3:
            self._context_menu.pop_up()

    def __init__(self, parent, widget):
        self._parent = parent
        self._context_menu = NagatoContextMenu(self)
        widget.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        widget.connect("button-press-event", self._on_button_press)
