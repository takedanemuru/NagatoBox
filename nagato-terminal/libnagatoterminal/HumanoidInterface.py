
from libnagatoterminal import CssProvider
from libnagatoterminal.util.Args import NagatoArgs
from libnagatoterminal.Window import NagatoWindow


class NagatoYuki(object):

    def N(self, message, user_data=None):
        if self._args.show_version:
            print("42.9.36")
        else:
            CssProvider.set_to_application()
            NagatoWindow()

    def __init__(self):
        self._args = NagatoArgs()
