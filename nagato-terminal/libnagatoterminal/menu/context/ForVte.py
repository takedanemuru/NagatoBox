
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.menu.Item import NagatoItem
from libnagatoterminal.menu.group.Clipboard import AsakuraClipboard
from libnagatoterminal.menu.group.GridActions import AsakuraGridActions
from libnagatoterminal.menu.item.action.AddNewTab import NagatoAddNewTab

class NagatoContextMenu(Gtk.Menu, NagatoObject):

    def pop_up(self, event):
        yuki_event_time = Gtk.get_current_event_time()
        self.popup(None, None, None, None, 0, yuki_event_time)

    def _initialize_children(self):
        AsakuraClipboard(self)
        self.append(Gtk.SeparatorMenuItem())
        AsakuraGridActions(self)
        self.append(Gtk.SeparatorMenuItem())
        NagatoAddNewTab(self)
        NagatoItem(self, "Close Current VTE", "YUKI.N > destroy")
        self.append(Gtk.SeparatorMenuItem())
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        Gtk.Menu.__init__(self)
        self._initialize_children()
        self.show_all()
