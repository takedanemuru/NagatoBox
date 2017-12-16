
from libnagatoterminal.util.Args import NagatoArgs


class NagatoVteOptions(object):

    def __init__(self, is_prime_vte, directory):
        self._args = NagatoArgs()
        self._is_prime_vte = is_prime_vte
        if directory is not None:
            self._directory = directory
        else:
            self._directory = self._args.get_vte_directory(is_prime_vte)

    @property
    def wait_for_command(self):
        return (self._is_prime_vte and self._args.command is not None)

    @property
    def directory(self):
        return self._directory

    @property
    def command(self):
        return "{} \n".format(self._args.command)

    @property
    def length(self):
        return len(self.command)
