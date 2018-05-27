
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.util import CssProvider
from libnagatoimageviewer.toolbaritem.DummyLabel import NagatoDummyLabel
from libnagatoimageviewer.toolbaritem.Button import NagatoButton
from libnagatoimageviewer.toolbaritem.FileButtons import AsakuraFileButtons
from libnagatoimageviewer.toolbaritem.ViewButtons import AsakuraViewButtons


class NagatoActionBar(Gtk.Box, NagatoObject):

    def _initialize_children(self):
        AsakuraFileButtons(self)
        NagatoDummyLabel(self)
        AsakuraViewButtons(self)
        NagatoDummyLabel(self)
        NagatoButton(self, "help-faq", "YUKI.N > about")
        NagatoButton(self, "application-exit", "YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        CssProvider.set_to_widget(self, "gtk-box-as-action-bar")
        self._initialize_children()
