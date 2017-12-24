
from gi.repository import Gtk
from libnagatoterminal.menu.Item import NagatoItem
from libnagatoterminal.menu.group.Clipboard import AsakuraClipboard
from libnagatoterminal.menu.group.GridActions import AsakuraGridActions
from libnagatoterminal.menu.item.action.AddNewTab import NagatoAddNewTab
from libnagatoterminal.menu.context.ContextCore import NagatoContextCore


class NagatoForVte(NagatoContextCore):

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
