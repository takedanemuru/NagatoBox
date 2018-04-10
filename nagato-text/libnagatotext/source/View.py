
from gi.repository import GtkSource
from libnagatotext.source.Buffer import NagatoBuffer
from libnagatotext.Prime import NagatoPrime
from libnagatotext.KeyBinds import NagatoKeyBinds
from libnagatotext.menu.context.ForSourceView import NagatoContextMenu


class NagatoView(GtkSource.View, NagatoPrime):

    def _yuki_n_clipboard(self, command):
        self._prime_object.clipboard(command)

    def _yuki_n_scheme(self, scheme):
        self._prime_object.set_scheme(scheme)

    def __init__(self, parent):
        self._parent = parent
        GtkSource.View.__init__(self)
        #self.set_show_line_numbers(True)
        self._prime_object = NagatoBuffer(self)
        NagatoKeyBinds(self)
        NagatoContextMenu(self)
        self._parent.add(self)
