
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.MenuItem import NagatoMenuItem
from libnagatoterminal.SubMenuVteNew import NagatoSubMenuVteNew
from libnagatoterminal.SubMenuVteExpand import NagatoSubMenuVteExpand
from libnagatoterminal.SubMenuVteShrink import NagatoSubMenuVteShrink


class NagatoContextMenu(Gtk.Menu, NagatoObject):

    def pop_up(self, event):
        yuki_event_time = Gtk.get_current_event_time()
        self.popup(None, None, None, None, 0, yuki_event_time)

    def _initialize_children(self):
        NagatoMenuItem(self, "Copy", "YUKI.N > copy")
        NagatoMenuItem(self, "Paste", "YUKI.N > paste")
        self.append(Gtk.SeparatorMenuItem())
        NagatoSubMenuVteNew(self)
        NagatoSubMenuVteExpand(self)
        NagatoSubMenuVteShrink(self)
        self.append(Gtk.SeparatorMenuItem())
        NagatoMenuItem(self, "Add New Tab", "YUKI.N > add new tab")
        NagatoMenuItem(self, "Close Current VTE", "YUKI.N > destroy")
        self.append(Gtk.SeparatorMenuItem())
        NagatoMenuItem(self, "About", "YUKI.N > about")
        NagatoMenuItem(self, "Quit", "YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        Gtk.Menu.__init__(self)
        self._initialize_children()
        self.show_all()
