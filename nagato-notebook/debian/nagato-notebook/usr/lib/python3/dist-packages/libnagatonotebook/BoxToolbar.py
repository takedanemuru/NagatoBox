
from gi.repository import Gtk
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.MenuButtonNew import NagatoMenuButtonNew
from libnagatonotebook.MenuButtonOpen import NagatoMenuButtonOpen
from libnagatonotebook.MenuButtonSave import NagatoMenuButtonSave
from libnagatonotebook.MenuButtonSaveAs import NagatoMenuButtonSaveAs


class NagatoBoxToolbar(Gtk.Box, NagatoObject):

    def _initialize_children(self):
        NagatoMenuButtonNew(self)
        NagatoMenuButtonOpen(self)
        NagatoMenuButtonSave(self)
        NagatoMenuButtonSaveAs(self)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Box.__init__(self)
        self._parent.attach(self, 0, 0, 1, 1)
        self.set_spacing(4)
        self._initialize_children()
