
from gi.repository import Gtk
from gi.repository import Gdk
from libnagato.Object import NagatoObject
from libnagato.menu.Item import NagatoItem


class NagatoContextCore(Gtk.Menu, NagatoObject):

    def _on_right_click(self, user_data=None):
        yuki_event_time = Gtk.get_current_event_time()
        self.popup(None, None, None, None, 0, yuki_event_time)

    def _on_middle_click(self, user_data=None):
        pass

    def _on_button_press(self, widget, event):
        if event.button == 2:
            self._on_middle_click()
        if event.button == 3:
            self._on_right_click()

    def _initialize_children(self):
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        self._parent.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self._parent.connect("button-press-event", self._on_button_press)
        Gtk.Menu.__init__(self)
        self._initialize_children()
        self.show_all()
