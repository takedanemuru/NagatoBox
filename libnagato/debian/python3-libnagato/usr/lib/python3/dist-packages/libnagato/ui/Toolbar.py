
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.util import CssProvider
from libnagato.toolbaritem.Spacer import NagatoSpacer
from libnagato.toolbaritem.Button import NagatoButton


class NagatoToolbar(Gtk.Box, NagatoObject):

    def _initialize_children(self):
        # samples
        NagatoSpacer(self)
        NagatoButton(self, "help-faq", "YUKI.N > about")
        NagatoButton(self, "application-exit", "YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        CssProvider.set_to_widget(self, "gtk-box-as-toolbar")
        self._initialize_children()
