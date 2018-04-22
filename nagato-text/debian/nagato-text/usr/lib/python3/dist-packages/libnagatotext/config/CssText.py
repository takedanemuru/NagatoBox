
from pathlib import Path
from libnagato.Object import NagatoObject
from libnagatotext.config.CssMainImage import NagatoCssMainImage
from libnagatotext.config.CssFont import NagatoCssFont


class NagatoCssText(NagatoObject):

    def _get_default_text(self):
        yuki_source = self._enquiry("YUKI.N > resources", "application.css")
        return Path(yuki_source).read_text()

    def _add_replacements(self):
        self._replacements.append(NagatoCssMainImage(self))
        self._replacements.append(NagatoCssFont(self))

    def get(self):
        yuki_text = self._get_default_text()
        for yuki_replacement in self._replacements:
            yuki_text = yuki_replacement.replace(yuki_text)
        return yuki_text

    def __init__(self, parent):
        self._parent = parent
        self._replacements = []
        self._add_replacements()
