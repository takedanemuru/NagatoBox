
from libnagato.Object import NagatoObject
from libnagatotext.PathEvents import NagatoPathEvents
from libnagatotext.dialog.FileChooserLoad import NagatoFileChooserLoad
from libnagatotext.dialog.FileChooserSave import NagatoFileChooserSave
from libnagatotext.dialog.WarningNotSaved import NagatoWarningNotSaved


class NagatoPathHandler(NagatoObject):

    def is_closable(self):
        yuki_response = NagatoWarningNotSaved.call()
        if yuki_response == 0:
            return False
        if yuki_response == 1:
            return True
        if yuki_response == 2:
            return self._path_events.save()

    def new(self):
        self._path_events.clear()

    def load(self):
        yuki_path = NagatoFileChooserLoad.call()
        if yuki_path is not None:
            self._path_events.load(yuki_path)

    def load_path(self, path):
        self._path_events.load(path)

    def save(self):
        self._path_events.save()

    def save_as(self):
        yuki_path = NagatoFileChooserSave.call()
        if yuki_path is not None:
            self._path_events.save_as(yuki_path)

    def __init__(self, parent):
        self._parent = parent
        self._path_events = NagatoPathEvents(self)
