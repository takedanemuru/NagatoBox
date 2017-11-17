
from gi.repository import Gtk
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.MenuItem import NagatoMenuItem


class NagatoContextMenuApplication(Gtk.Menu, NagatoObject):

    def pop_up(self, event):
        yuki_event_time = Gtk.get_current_event_time()
        self.popup(None, None, None, None, 0, yuki_event_time)

    def _initialize_children(self):
        NagatoMenuItem(self, "New", "YUKI.N > file new")
        NagatoMenuItem(self, "Open", "YUKI.N > file open")
        NagatoMenuItem(self, "Save", "YUKI.N > file save")
        NagatoMenuItem(self, "Save As", "YUKI.N > file save as")
        self.append(Gtk.SeparatorMenuItem())
        NagatoMenuItem(self, "About", "YUKI.N > about")
        NagatoMenuItem(self, "Quit", "YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        Gtk.Menu.__init__(self)
        self._initialize_children()
        self.show_all()
