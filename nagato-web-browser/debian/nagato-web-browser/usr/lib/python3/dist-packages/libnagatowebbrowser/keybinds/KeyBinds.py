
from gi.repository import Gdk
from libnagato.Object import NagatoObject
from libnagatowebbrowser.util.TimeDeltaLock import NagatoTimeDeltaLock
from libnagatowebbrowser.keybinds.Accelerator import NagatoAccelerator


class NagatoKeyBinds(NagatoObject):

    def _dispatch(self, event_state, keyval_name):
        for yuki_accelerator in self._accelerators:
            if yuki_accelerator(event_state, keyval_name):
                break

    def _on_key_press(self, widget, event, user_data=None):
        if self._time_delta_lock.check_diff(0.2):
            self._dispatch(event.state, Gdk.keyval_name(event.keyval))

    def _add(self, mask, binds, values):
        yuki_accelerator = NagatoAccelerator(self, mask, binds, values)
        self._accelerators.append(yuki_accelerator)

    def _initialize_accelerators(self):
        pass

    def __init__(self, parent):
        self._parent = parent
        self._parent.connect("key-press-event", self._on_key_press)
        self._time_delta_lock = NagatoTimeDeltaLock()
        self._accelerators = []
        self._initialize_accelerators()
