
from time import sleep
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator
from libnagatowebbrowser.menu.group.Navigations import AsakuraNavigations
from libnagatowebbrowser.menu.group.Image import AsakuraImage
from libnagatowebbrowser.menu.group.Link import AsakuraLink
from libnagatowebbrowser.menu.action.CloseTab import NagatoCloseTab

class NagatoForWebView(Gtk.Menu, NagatoObject):

    def pop_up(self, hit_test_result):
        #"this method is NOT GTK+ callback,
        # doesn't have event argument.
        self.show_all()
        yuki_event_time = Gtk.get_current_event_time()
        self.popup(None, None, None, None, 0, yuki_event_time)
        
    def _initialize_children(self):
        AsakuraNavigations(self)
        AsakuraImage(self)
        AsakuraLink(self)
        NagatoItem(self, "Add New Tab", "YUKI.N > add new tab")
        NagatoCloseTab(self)
        NagatoSeparator(self)
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        Gtk.Menu.__init__(self)
        self._initialize_children()
