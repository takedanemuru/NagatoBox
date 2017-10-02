

PATH_TEMPLATE = "/proc/{0}/task/{0}/children"


class NagatoProcessWatcher(object):

    def _get_child(self):
        yuki_file = open(self._path, "r")
        return yuki_file.read()

    def __init__(self, parent_pid):
        self._path = PATH_TEMPLATE.format(parent_pid)

    @property
    def child(self):
        return self._get_child()

    @property
    def can_close(self):
        if self._get_child() == "":
            return True
        return False
