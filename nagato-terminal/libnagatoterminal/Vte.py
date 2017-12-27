
import gi

gi.require_version("Vte", "2.91")

from gi.repository import Vte
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagatoterminal.ProcessWatcher import NagatoProcessWatcher
from libnagatoterminal.VteAttributes import NagatoVteAttributes
from libnagatoterminal.UserInput import NagatoUserInput
from libnagatoterminal.TabLabel import NagatoTabLabel
from libnagatoterminal.VteOptions import NagatoVteOptions


class NagatoVte(Vte.Terminal, NagatoObject):

    def _initialize_vte_widget(self):
        Vte.Terminal.__init__(self)
        yuki_is_synced, yuki_pid = self.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            self._options.directory,
            ["/bin/bash"],
            None,
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            None
            )
        return yuki_pid

    def _initialize_vte(self):
        yuki_pid = self._initialize_vte_widget()
        self._watcher = NagatoProcessWatcher(yuki_pid)
        self._tab_label.set_title("PID : {}".format(yuki_pid))
        if self._options.wait_for_command:
            self.feed_child(self._options.command, self._options.length)

    def _initialize_first_page(self):
        self._parent.insert_page(self, self._tab_label, -1)
        self._parent.set_tab_reorderable(self, True)
        self.show_all()
        # notebook reject to switch page when children aren't visible.
        self._parent.set_current_page(self._parent.get_n_pages() - 1)

    def _yuki_n_copy(self):
        self.copy_clipboard()

    def _yuki_n_paste(self):
        self.paste_clipboard()

    def _yuki_n_destroy(self):
        if self._watcher.can_close_with_user_response():
            self.destroy()
            self._tab_label.destroy()
            self._raise("YUKI.N > child destroyed")

    def _inform_working_directory(self):
        return self._watcher.working_directory

    def _inform_has_selection(self):
        return self.get_has_selection()

    def __init__(self, parent, is_prime_vte, directory=None):
        self._parent = parent
        self._tab_label = NagatoTabLabel(parent)
        self._options = NagatoVteOptions(is_prime_vte, directory)
        self._initialize_vte()
        NagatoVteAttributes(self)
        NagatoUserInput(self)
        self._initialize_first_page()

    @property
    def child_process(self):
        return self._watcher.child
