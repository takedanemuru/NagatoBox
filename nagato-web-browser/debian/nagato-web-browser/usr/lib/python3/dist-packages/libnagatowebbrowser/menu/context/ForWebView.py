
from time import sleep
from gi.repository import Gtk
from libnagatowebbrowser.CoreObject import NagatoObject
from libnagatowebbrowser.menu.Item import NagatoItem
from libnagatowebbrowser.menu.group.Navigations import NagatoNavigations
from libnagatowebbrowser.menu.group.Image import NagatoImage
from libnagatowebbrowser.menu.group.Link import NagatoLink
from libnagatowebbrowser.menu.Separator import NagatoSeparator
from libnagatowebbrowser.menu.item.sensitive.CloseCurrentTab import (
    NagatoCloseCurrentTab
    )

class NagatoForWebView(Gtk.Menu, NagatoObject):

    def _toggle(self, hit_test_result):
        for yuki_group in self._groups:
            yuki_group.toggle(hit_test_result)

    def pop_up(self, hit_test_result):
        #"this method is NOT GTK+ callback,
        # doesn't have event argument.
        # yuki_context = hit_test_result.get_context()
        # print(yuki_context)
        self.show_all()
        self._toggle(hit_test_result)
        yuki_event_time = Gtk.get_current_event_time()
        self.popup(None, None, None, None, 0, yuki_event_time)
        
    def _initialize_children(self):
        self._groups = []
        self._groups.append(NagatoNavigations(self))
        self._groups.append(NagatoImage(self))
        self._groups.append(NagatoLink(self))
        NagatoItem(self, "Add New Tab", "YUKI.N > add new tab")
        NagatoCloseCurrentTab(self, self)
        NagatoSeparator(self)
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        Gtk.Menu.__init__(self)
        self.get_style_context().add_class("context-menu")
        self._initialize_children()
