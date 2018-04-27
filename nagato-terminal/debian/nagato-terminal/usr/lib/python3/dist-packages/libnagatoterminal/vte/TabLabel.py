
from gi.repository import Gtk
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagatoterminal.menu.context.ForNotebookTabLabel import (
    NagatoContextMenu
    )
from libnagatoterminal.dialog.SetTabTitle import NagatoSetTabTitle


class NagatoTabLabel(Gtk.EventBox, NagatoObject):

    def _initialize_label(self):
        self._label = Gtk.Label("untitled")
        self._label.set_can_focus(False)
        self.add(self._label)

    def _yuki_n_set_tab_title(self):
        yuki_title = NagatoSetTabTitle.call(self._label.get_text())
        if yuki_title != "":
            self._user_defined = True
            self._label.set_text(yuki_title)
            self.show_all()

    def set_title(self, title):
        if title is not None and not self._user_defined:
            self._label.set_text(GLib.basename(title))
            self.show_all()

    def __init__(self, parent, container):
        self._parent = parent
        Gtk.EventBox.__init__(self)
        self._user_defined = False
        self._initialize_label()
        NagatoContextMenu(self)
        self.show_all()
