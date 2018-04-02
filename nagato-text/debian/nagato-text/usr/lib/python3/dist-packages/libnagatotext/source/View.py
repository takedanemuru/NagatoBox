
from gi.repository import GtkSource
from libnagatotext.source.Buffer import NagatoBuffer
from libnagatotext.Prime import NagatoPrime
from libnagatotext.KeyBinds import NagatoKeyBinds


class NagatoView(GtkSource.View, NagatoPrime):

    def _yuki_n_new(self):
        self._buffer.new()

    def _yuki_n_load(self):
        self._buffer.load()

    def _yuki_n_save(self):
        self._buffer.save()

    def _yuki_n_save_as(self):
        self._buffer.save_as()

    def __init__(self, parent):
        self._parent = parent
        GtkSource.View.__init__(self)
        self._buffer = NagatoBuffer(self)
        NagatoKeyBinds(self)
        self._parent.add(self)
