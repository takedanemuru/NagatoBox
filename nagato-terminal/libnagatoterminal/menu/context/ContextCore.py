
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoContextCore(Gtk.Menu, NagatoObject):

    def pop_up(self, user_data=None):
        yuki_event_time = Gtk.get_current_event_time()
        self.popup(None, None, None, None, 0, yuki_event_time)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Menu.__init__(self)
        self.get_style_context().add_class("context-menu")
        self._initialize_children()
        self.show_all()


