
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoContextCore(Gtk.Menu, NagatoObject):

    def pop_up(self, user_data=None):
        yuki_event_time = Gtk.get_current_event_time()
        self.popup(None, None, None, None, 0, yuki_event_time)

    def _initialize_self(self):
        Gtk.Menu.__init__(self)

    def __init__(self, parent):
        self._parent = parent
        self._initialize_self()
        self._initialize_children()
        self.show_all()


