
import os
from libnagatoterminal.dialog import Portal as Dialog

PATH_TEMPLATE = "/proc/{0}/task/{0}/children"
DIRECTORY_TEMPLATE = "/proc/{0}/cwd"
COMMAND_TEMPLATE = "/proc/{0}/comm"


class NagatoProcessWatcher(object):

    def _get_process_name(self, process_id):
        yuki_path = COMMAND_TEMPLATE.format(int(process_id))
        return open(yuki_path, "r").read().rstrip()

    def _get_child(self):
        yuki_child_id = open(self._path, "r").read()
        if yuki_child_id == "":
            return None
        return self._get_process_name(int(yuki_child_id))

    def __init__(self, parent_pid):
        self._path = PATH_TEMPLATE.format(parent_pid)
        self._directory = DIRECTORY_TEMPLATE.format(parent_pid)

    def can_close_with_user_response(self):
        return Dialog.get_can_close_vte(self._get_child())

    @property
    def working_directory(self):
        return os.readlink(self._directory)

    @property
    def child(self):
        return self._get_child()
