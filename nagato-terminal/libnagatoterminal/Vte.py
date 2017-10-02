import gi

gi.require_version("Vte", "2.91")

from gi.repository import Vte
from gi.repository import GLib
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.ProcessWatcher import NagatoProcessWatcher
from libnagatoterminal.VteAttributes import NagatoVteAttributes
from libnagatoterminal.UserInput import NagatoUserInput
from libnagatoterminal.util.Args import NagatoArgs


class NagatoVte(Vte.Terminal, NagatoObject):

    def _initialize_vte_widget(self, is_prime_vte):
        Vte.Terminal.__init__(self)
        yuki_is_synced, yuki_pid = self.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            self._args.get_vte_directory(is_prime_vte),
            ["/bin/bash"],
            None,
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            None)
        return yuki_pid

    def _initialize_vte(self, is_prime_vte):
        yuki_pid = self._initialize_vte_widget(is_prime_vte)
        self._watcher = NagatoProcessWatcher(yuki_pid)
        if is_prime_vte:
            self._send_command(self._args.command)

    def _send_command(self, command=None):
        if command:
            yuki_command = "{} \n".format(command)
            self.feed_child(yuki_command, len(yuki_command))

    def __init__(self, parent, is_prime_vte, rect):
        self._parent = parent
        self._args = NagatoArgs()
        self._initialize_vte(is_prime_vte)
        NagatoVteAttributes(self)
        NagatoUserInput(self)
        self._initialize_ext(rect)
        parent.attach(self, rect.left, rect.top, 1, 1)

    def _yuki_n_copy(self):
        self.copy_clipboard()

    def _yuki_n_paste(self):
        self.paste_clipboard()

    def _yuki_n_destroy(self):
        if self._watcher.can_close_with_user_response():
            self.destroy()
            self._raise("YUKI.N > child destroyed")

    @property
    def can_close(self):
        return self._watcher.can_close
