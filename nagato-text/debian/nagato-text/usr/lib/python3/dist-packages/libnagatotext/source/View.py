
from gi.repository.GtkSource import View
from libnagatotext.source.Buffer import NagatoBuffer
from libnagatotext.Prime import NagatoPrime
from libnagatotext.KeyBinds import NagatoKeyBinds
from libnagatotext.menu.context.ForSourceView import NagatoContextMenu
from libnagatotext.source.ViewConfig import NagatoViewConfig


class NagatoView(View, NagatoPrime):

    def _yuki_n_files(self, command):
        self._prime_object.prime_call("YUKI.N > {}".format(command))

    def _yuki_n_open_file(self, path):
        self._prime_object.prime_call("YUKI.N > open file", path)

    def _yuki_n_clipboard(self, command):
        self._prime_object.clipboard(command)

    def _yuki_n_scheme(self, scheme):
        self._prime_object.set_scheme(scheme)

    def _yuki_n_search_and_replace(self):
        self._prime_object.search_and_replace()

    def _yuki_n_config(self, user_data):
        self._raise("YUKI.N > config", user_data)
        self._config.refresh()

    def __init__(self, parent):
        self._parent = parent
        View.__init__(self)
        self._config = NagatoViewConfig(self)
        self._prime_object = NagatoBuffer(self)
        NagatoKeyBinds(self)
        NagatoContextMenu(self)
        self._parent.add(self)
