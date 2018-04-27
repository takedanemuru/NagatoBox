
from libnagato.Object import NagatoObject


class NagatoCommand(NagatoObject):

    def _get_command(self):
        yuki_command = self._enquiry("YUKI.N > args", "command")
        return "{} \n".format(yuki_command)

    def _wait_for_command(self):
        yuki_command = self._enquiry("YUKI.N > args", "command")
        return (self._is_prime_vte and yuki_command is not None)

    def execute(self):
        if self._wait_for_command():
            self._raise("YUKI.N > feed child", self._get_command())

    def __init__(self, parent, is_prime_vte):
        self._parent = parent
        self._is_prime_vte = is_prime_vte
