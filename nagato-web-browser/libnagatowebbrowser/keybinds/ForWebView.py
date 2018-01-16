
from libnagatowebbrowser.keybinds.KeyBinds import NagatoKeyBinds as TFEI
from libnagatowebbrowser.keybinds import Mask

MESSAGES_FOR_NONE = {
    "F5": "YUKI.N > reload",
    "F11": "YUKI.N > toggle fullscreen"
}

MESSAGES_FOR_ALT = {
    "Left": "YUKI.N > go back",
    "Right": "YUKI.N > go forward"
}

MESSAGES_FOR_CTRL = {
    "f": "YUKI.N > inpage search",
    "n": "YUKI.N > add new tab",
    "p": "YUKI.N > snapshot",
    "u": "YUKI.N > dialog url"
}

VALUES_FOR_CTRL = {
    "p": 0
}


class NagatoKeyBinds(TFEI):

    def _initialize_accelerators(self):
        self._add(None, MESSAGES_FOR_NONE, {})
        self._add(Mask.ALT, MESSAGES_FOR_ALT, {})
        self._add(Mask.CTRL, MESSAGES_FOR_CTRL, VALUES_FOR_CTRL)
