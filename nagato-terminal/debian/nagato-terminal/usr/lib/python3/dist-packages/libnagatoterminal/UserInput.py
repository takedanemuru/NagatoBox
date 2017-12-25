from libnagato.Object import NagatoObject
from libnagatoterminal.KeyBinds import NagatoKeyBinds
from libnagatoterminal.input.mouse.ForVte import NagatoForVte


class NagatoUserInput(NagatoObject):

    def __init__(self, parent):
        self._parent = parent
        NagatoKeyBinds(self, parent)
        NagatoForVte(self, parent)
