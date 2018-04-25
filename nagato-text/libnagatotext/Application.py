
from libnagato.application.Application import NagatoApplication as TFEI
from libnagatotext.MainWindow import NagatoMainWindow
from libnagatotext.config.CssMainImage import NagatoCssMainImage
from libnagatotext.config.CssFont import NagatoCssFont


class NagatoApplication(TFEI):

    def _initialize_css_replacements(self):
        self._append_css_replacement(NagatoCssMainImage(self))
        self._append_css_replacement(NagatoCssFont(self))

    def run(self):
        NagatoMainWindow(self)
