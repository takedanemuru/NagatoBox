
from libnagatokeycode.eventbox.EventBox import NagatoEventBox as TFEI
from libnagatokeycode.menu.context.ForLabel import NagatoContextMenu
from libnagatokeycode.KeyBinds import NagatoKeyBinds
from libnagatokeycode.DummyLabel import NagatoDummyLabel

class NagatoEventBox(TFEI):

    def _yuki_n_keyval(self, keyval):
        self._label.set_keyval(keyval)

    def _yuki_n_say(self, something):
        self._label.say(something)

    def _yuki_n_hello_world(self):
        self._label.hello_world()

    def _on_initialize(self):
        NagatoKeyBinds(self)
        self._label = NagatoDummyLabel(self)
