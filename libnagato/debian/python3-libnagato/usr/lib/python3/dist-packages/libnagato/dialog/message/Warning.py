
from libnagato.dialog.message.Message import NagatoMessage
from libnagato.dialog.ui.Label import NagatoLabel


class NagatoWarning(NagatoMessage):

    @classmethod
    def call(cls, title="warning", message="", pixbuf=None, buttons=["OK"]):
        yuki_dialog = NagatoWarning(title, message, pixbuf, buttons)
        yuki_response = yuki_dialog.run()
        yuki_dialog.destroy()
        return yuki_response

    def _set_contents(self, message):
        NagatoLabel(self._content_area, message, "dialog-warning")
