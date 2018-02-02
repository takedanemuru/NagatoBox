
from gi.repository import Gtk
from gi.repository import Pango
from libnagato.Object import NagatoObject
from libnagatowebbrowser.menu.context.ForTabLabel import NagatoContextMenu

class NagatoLabel(NagatoObject, Gtk.EventBox):

    def set_text(self, title):
        self._label.set_text(title)

    def __init__(self, parent, mode=Pango.EllipsizeMode.END):
        # Gtk.Label should be wrapped in Gtk.EventBox.
        # to get button-press-event.
        self._parent = parent
        Gtk.EventBox.__init__(self)
        self._label = Gtk.Label()
        self._label.set_ellipsize(mode)
        self._label.set_padding(0, 0)
        self.add(self._label)
        NagatoContextMenu(self)
