
from datetime import datetime
from libnagato.Object import NagatoObject
from libnagatoscreenshot.WindowSurface import NagatoWindowSurface
from libnagatoscreenshot.MainWindow import NagatoMainWindow
from libnagatoscreenshot.Sound import NagatoSound
from libnagatoscreenshot.dialog.WindowNotFound import NagatoWindowNotFound

FORMAT = "screenshot_%Y-%m-%d_%H:%M:%S"
SOUND = "sounds/camera-snap.wav"


class NagatoScreenshot(NagatoObject):

    def _yuki_n_save_to(self, path):
        self._surface.save_to(path)

    def _inform_surface(self):
        return self._surface.get_surface()

    def _inform_time_stamp(self):
        return self._time_stamp

    def _activate(self):
        if self._surface.get_surface() is not None:
            self._sound.play(self._resources.get_absolute_path(SOUND))
            NagatoMainWindow(self, self._args, self._resources)
        else:
            print("YUKI.N > focused window not found.")
            NagatoWindowNotFound.call()

    def __init__(self, args, resources):
        self._parent = None
        self._args = args
        self._resources = resources
        self._sound = NagatoSound()
        self._surface = NagatoWindowSurface(self._args["focus"])
        self._time_stamp = datetime.now().strftime(FORMAT)
        self._activate()
