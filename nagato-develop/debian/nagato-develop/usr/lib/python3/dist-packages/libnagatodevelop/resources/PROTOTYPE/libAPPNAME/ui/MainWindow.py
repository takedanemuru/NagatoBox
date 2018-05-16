
from libnagato.ui.MainWindow import NagatoMainWindow as TFEI
from libnagato.dialog.message.Warning import NagatoWarning
from libAPPNAME.eventbox.ForGrid import NagatoEventBox
from libAPPNAME.Mikuru import DialogArgs


class NagatoMainWindow(TFEI):

    def _on_close_window(self, widget, event, user_data=None):
        if NagatoWarning.call(**DialogArgs.QUIT) == 0:
            return True
        return self._gtk_main_quit()

    def _on_initialize(self):
        NagatoEventBox(self)
