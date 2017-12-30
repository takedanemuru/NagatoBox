
import os
from libnagatoterminal.util.Args import NagatoArgs


class NagatoVteOptions(object):

    def __init__(self, is_prime_vte, directory):
        self._args = NagatoArgs()
        self._is_prime_vte = is_prime_vte
        self._directory = directory

    def get_command(self):
        yuki_command = "{} \n".format(self._args["command"])
        return yuki_command, len(yuki_command)

    @property
    def wait_for_command(self):
        return (self._is_prime_vte and self._args["command"] is not None)

    @property
    def directory(self):
        if self._directory is not None:
            return self._directory
        if self._is_prime_vte:
            return self._args["directory"]
        return os.environ["HOME"]
