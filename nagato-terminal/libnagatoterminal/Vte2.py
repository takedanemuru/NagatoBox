
import gi

gi.require_version("Vte", "2.91")

from gi.repository import Vte
from gi.repository import GLib
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.ProcessWatcher import NagatoProcessWatcher
from libnagatoterminal.VteAttributes import NagatoVteAttributes
from libnagatoterminal.UserInput import NagatoUserInput
from libnagatoterminal.util.Args import NagatoArgs
from libnagatoterminal.TabLabel import NagatoTabLabel


class NagatoVte(Vte.Terminal, NagatoObject):

    def _initialize_vte_widget(self):
        Vte.Terminal.__init__(self)
        yuki_is_synced, yuki_pid = self.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            self._directory,
            ["/bin/bash"],
            None,
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            None)
        return yuki_pid

    def _initialize_vte(self, is_prime_vte):
        yuki_pid = self._initialize_vte_widget()
        self._watcher = NagatoProcessWatcher(yuki_pid)
        self._tab_label.set_title("PID : {}".format(yuki_pid))
        if is_prime_vte:
            self._send_command(self._args.command)

    def _send_command(self, command=None):
        if command is not None:
            yuki_command = "{} \n".format(command)
            self.feed_child(yuki_command, len(yuki_command))

    def _set_directory(self, is_prime_vte, directory):
        self._args = NagatoArgs()
        if directory is not None:
            self._directory = directory
        else:
            self._directory = self._args.get_vte_directory(is_prime_vte)

    def __init__(self, parent, is_prime_vte, directory=None):
        self._parent = parent
        self._tab_label = NagatoTabLabel(parent)
        self._set_directory(is_prime_vte, directory)
        self._initialize_vte(is_prime_vte)
        NagatoVteAttributes(self)
        NagatoUserInput(self)
        parent.insert_page(self, self._tab_label, -1)
        parent.set_tab_reorderable(self, True)
        self.show_all()
        # notebook reject to switch page when children aren't visible.
        parent.set_current_page(parent.get_n_pages() - 1)

    def _yuki_n_add_new_tab(self):
        self._raise(
            "YUKI.N > add new tab",
            self._watcher.working_directory
            )

    def _yuki_n_copy(self):
        self.copy_clipboard()

    def _yuki_n_paste(self):
        self.paste_clipboard()

    def _yuki_n_destroy(self):
        if self._watcher.can_close_with_user_response():
            self.destroy()
            self._tab_label.destroy()
            self._raise("YUKI.N > child destroyed")

    @property
    def child_process(self):
        return self._watcher.child
