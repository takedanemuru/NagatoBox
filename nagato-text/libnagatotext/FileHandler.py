
from libnagatotext.PathEvents import NagatoPathEvents
from libnagatotext.Prime import NagatoPrime
from libnagatotext.source.SaveState import NagatoSaveState
from libnagatotext.dialog.FileChooserLoad import NagatoFileChooserLoad
from libnagatotext.dialog.FileChooserSave import NagatoFileChooserSave


class NagatoFileHandler(NagatoPrime):

    def _is_closable(self):
        yuki_response = self._save_state.get_save_state()
        if yuki_response is not None:
            return yuki_response
        return self._path_handler.save()

    def _yuki_n_path_event(self, user_data):
        yuki_message, yuki_data = user_data
        self._raise("YUKI.N > {}".format(yuki_message), yuki_data)
        self._save_state.set_state_to_saved()

    def _yuki_n_new(self):
        if self._is_closable():
            self._path_handler.new()

    def _yuki_n_load(self):
        if not self._is_closable():
            return
        yuki_path = NagatoFileChooserLoad.call()
        if yuki_path is not None:
            self._path_handler.load(yuki_path)

    def _yuki_n_save(self):
        self._path_handler.save()

    def _yuki_n_save_as(self):
        yuki_path = NagatoFileChooserSave.call()
        if yuki_path is not None:
            self._path_handler.save_as(yuki_path)

    def __init__(self, parent, text_buffer):
        self._parent = parent
        self._save_state = NagatoSaveState(text_buffer)
        self._path_handler = NagatoPathEvents(self)
