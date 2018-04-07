
from libnagato.Object import NagatoObject


class NagatoShowVersion(NagatoObject):

    def _set_option(self):
        self._parent.add_argument(
            "-v",
            "--version",
            action="store_true",
            dest="show_version",
            default=False,
            help="show version"
            )

    def __init__(self, parent):
        self._parent = parent
        self._set_option()
