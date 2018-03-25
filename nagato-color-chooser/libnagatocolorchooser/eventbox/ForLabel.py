
from libnagatocolorchooser.eventbox.EventBox import NagatoEventBox as TFEI
from libnagatocolorchooser.menu.context.ForLabel import NagatoContextMenu
from libnagatocolorchooser.DummyLabel import NagatoDummyLabel

class NagatoEventBox(TFEI):

    def _yuki_n_say(self, something):
        self._label.say(something)

    def _yuki_n_hello_world(self):
        self._label.hello_world()

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._label = NagatoDummyLabel(self)