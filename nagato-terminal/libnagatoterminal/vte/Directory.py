
from gi.repository import GLib
from libnagato.Object import NagatoObject


class NagatoDirectory(NagatoObject):

    def get(self):
        if self._directory is not None:
            return self._directory
        if self._is_prime_vte:
            return self._enquiry("YUKI.N > args", "directory")
        return GLib.get_home_dir()

    def __init__(self, parent, is_prime_vte, directory):
        self._parent = parent
        self._is_prime_vte = is_prime_vte
        self._directory = directory
