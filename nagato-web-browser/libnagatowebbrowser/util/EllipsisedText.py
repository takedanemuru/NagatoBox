
from gi.repository import Pango


class NagatoEllipsesedText(object):

    def get(self, text):
        self._pango_layout.set_text(text, 40)
        yuki_text = self._pango_layout.get_text()
        if len(text) > 40:
            yuki_text += "..."
        return yuki_text

    def __init__(self):
        self._pango_context = Pango.Context()
        self._pango_layout = Pango.Layout(self._pango_context)
        self._pango_layout.set_ellipsize(Pango.EllipsizeMode.END)
