
from libnagato.ui.MainWindow import NagatoMainWindow as TFEI
from libnagato.dialog.message.Warning import NagatoWarning
from libnagatodevelop.eventbox.ForGrid import NagatoEventBox
from libnagatodevelop.ApplicationModel import NagatoApplicationModel
from libnagatodevelop.Mikuru import DialogArgs


class NagatoMainWindow(TFEI):

    def _yuki_n_force_quit(self):
        self._gtk_main_quit()

    def _yuki_n_create(self):
        self._model.create()

    def _yuki_n_model(self, user_data):
        pass

    def _inform_model(self):
        return self._model

    def _on_close_window(self, widget, event, user_data=None):
        if NagatoWarning.call(**DialogArgs.QUIT) == 0:
            return True
        return self._gtk_main_quit()

    def _on_initialize(self):
        self._model = NagatoApplicationModel(self)
        NagatoEventBox(self)
