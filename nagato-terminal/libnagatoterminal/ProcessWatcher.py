
import os
from gi.repository import Gtk
from libnagatoterminal.Dialog import NagatoDialog

PATH_TEMPLATE = "/proc/{0}/task/{0}/children"
DIRECTORY_TEMPLATE = "/proc/{0}/cwd"
COMMAND_TEMPLATE = "/proc/{0}/comm"

class NagatoProcessWatcher(object):

    def _get_child(self):
        yuki_file = open(self._path, "r")
        return yuki_file.read()

    def __init__(self, parent_pid):
        self._path = PATH_TEMPLATE.format(parent_pid)
        self._directory = DIRECTORY_TEMPLATE.format(parent_pid)

    def can_close_with_user_response(self):
        if self.child is None:
            return True
        else:
            yuki_dialog = NagatoDialog()
            yuki_response = yuki_dialog.run()
            yuki_dialog.destroy()
            return (yuki_response == Gtk.ResponseType.OK)

    @property
    def working_directory(self):
        return os.readlink(self._directory)

    @property
    def child(self):
        yuki_child_process = self._get_child()
        if yuki_child_process == "":
            return None
        yuki_path = COMMAND_TEMPLATE.format(int(yuki_child_process))
        yuki_command = open(yuki_path, "r")
        return yuki_command.read().rstrip()
