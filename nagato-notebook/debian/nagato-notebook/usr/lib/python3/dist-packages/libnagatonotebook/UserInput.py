
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.GSound import NagatoGSound


class NagatoUserInput(NagatoObject):

    def _on_key_press(self, widget, event):
        if event.keyval == 65293:
            self._gsound.play("complete")
        else:
            self._gsound.play("bell")

    def _on_preedit_changed(self, text_view, preedit):
        self._gsound.play("bell")

    def __init__(self, parent):
        self._parent = parent
        self._gsound = NagatoGSound()
        self._parent.connect("key-press-event", self._on_key_press)
        self._parent.connect("preedit-changed", self._on_preedit_changed)
