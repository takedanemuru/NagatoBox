from gi.repository import Gdk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.ContextMenu import NagatoContextMenu


class NagatoMouseBinds(NagatoObject):

    def _on_button_press(self, widget, event):
        if event.button == 3:
            self._context_menu.pop_up(event)

    def __init__(self, parent, vte):
        self._parent = parent
        self._context_menu = NagatoContextMenu(self)
        vte.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        vte.connect("button-press-event", self._on_button_press)