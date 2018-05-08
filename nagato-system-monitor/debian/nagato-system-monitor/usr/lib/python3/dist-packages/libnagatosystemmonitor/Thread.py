
import threading
import time
from gi.repository import GLib
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.observer.Facade import NagatoFacade

INTERVAL = 2


class NagatoThread(NagatoObject):

    def _target(self):
        while self._enabled:
            GLib.idle_add(self._facade.step, None, priority=GLib.PRIORITY_LOW)
            time.sleep(INTERVAL)
        self._raise("YUKI.N > stopped")

    def stop(self):
        self._enabled = False

    def start(self):
        self._enabled = True
        self._thread.start()

    def __init__(self, parent):
        self._parent = parent
        self._facade = NagatoFacade(self)
        self._enabled = False
        self._thread = threading.Thread(target=self._target)
        self._thread.daemon = True
