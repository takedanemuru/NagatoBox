
from libnagatoscreenshot.eventbox.EventBox import NagatoEventBox as TFEI
from libnagatoscreenshot.menu.context.ForLabel import NagatoContextMenu
from libnagatoscreenshot.DummyLabel import NagatoDummyLabel

class NagatoEventBox(TFEI):

    def _yuki_n_say(self, something):
        self._label.say(something)

    def _yuki_n_hello_world(self):
        self._label.hello_world()

    def _on_initialize(self):
        NagatoContextMenu(self)
        self._label = NagatoDummyLabel(self)