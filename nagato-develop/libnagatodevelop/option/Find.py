
from libnagato.Object import NagatoObject


class NagatoFind(NagatoObject):

    def _set_option(self):
        self._parent.add_argument(
            "-f",
            "--find",
            dest="find",
            type=str,
            nargs=1,
            metavar="KEYWORD",
            help="find keyword"
            )

    def __init__(self, parent):
        self._parent = parent
        self._set_option()

