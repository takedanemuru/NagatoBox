
from gi.repository import Vte
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagatoterminal.vte.Directory import NagatoDirectory
from libnagatoterminal.vte.Command import NagatoCommand


class NagatoOptions(NagatoObject):

    def __init__(self, parent, is_prime_vte, directory):
        self._parent = parent
        self._is_prime_vte = is_prime_vte
        self._directory = NagatoDirectory(self, is_prime_vte, directory)
        self._command = NagatoCommand(self, is_prime_vte)

    def spawn_sync(self):
        yuki_is_synced, yuki_pid = self._parent.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            self._directory.get(),
            ["/bin/bash"],
            None,
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            None
            )
        self._raise("YUKI.N > vte initialized", yuki_pid)
        self._command.execute()
