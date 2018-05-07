
from gi.repository import Vte
from libnagato.Object import NagatoObject
from libnagatoterminal.vte.Attributes import NagatoAttributes
from libnagatoterminal.vte.Options import NagatoOptions
from libnagatoterminal.keyboard.Binds import NagatoBinds
from libnagatoterminal.menu.context.ForVte import NagatoContextMenu


class NagatoVte(NagatoObject, Vte.Terminal):

    def _yuki_n_feed_child(self, command):
        self.feed_child(command, len(command))

    def _yuki_n_copy(self):
        self.copy_clipboard()

    def _yuki_n_paste(self):
        self.paste_clipboard()

    def _inform_has_selection(self):
        return self.get_has_selection()

    def __init__(self, parent, is_prime_vte, directory=None):
        self._parent = parent
        self._options = NagatoOptions(self, is_prime_vte, directory)
        Vte.Terminal.__init__(self)
        self._options.spawn_sync()
        self._attributes = NagatoAttributes(self)
        NagatoBinds(self)
        NagatoContextMenu(self)

    def refresh_attributes(self):
        self._attributes.refresh()

    @property
    def child_process(self):
        return self._enquiry("YUKI.N > child process")
