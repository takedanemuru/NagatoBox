from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal.KeyBinds import NagatoKeyBinds
from libnagatoterminal.MouseBinds import NagatoMouseBinds


class NagatoUserInput(NagatoObject):

    def __init__(self, parent):
        self._parent = parent
        NagatoKeyBinds(self, parent)
        NagatoMouseBinds(self, parent)
