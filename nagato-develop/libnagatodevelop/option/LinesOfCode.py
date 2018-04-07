
from libnagato.Object import NagatoObject


class NagatoLinesOfCode(NagatoObject):

    def _set_option(self):
        self._parent.add_argument(
            "-l",
            "--lines-of-code",
            action="store_true",
            dest="lines_of_code",
            default=False,
            help="show lines of code"
            )

    def __init__(self, parent):
        self._parent = parent
        self._set_option()
