
from libnagato.dialog.message.Message import NagatoMessage
from libnagato.dialog.ui.Label import NagatoLabel


class NagatoInfo(NagatoMessage):

    @classmethod
    def call(cls, title="info", message="", pixbuf=None, buttons=["OK"]):
        yuki_dialog = NagatoInfo(title, message, pixbuf, buttons)
        yuki_response = yuki_dialog.run()
        yuki_dialog.destroy()
        return yuki_response

    def _set_contents(self, message):
        NagatoLabel(self._content_area, message, "dialog-info")

