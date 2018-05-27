
from libnagato.application.Application import NagatoApplication as TFEI
from libnagato.config.CssMainImage import NagatoCssMainImage
from libnagato.config.CssFont import NagatoCssFont
from libnagatosystemmonitor.MainWindow import NagatoMainWindow
from libnagatosystemmonitor.ui.MiniWindow import NagatoMiniWindow


class NagatoApplication(TFEI):

    def _initialize_css_replacements(self):
        self._append_css_replacement(NagatoCssMainImage(self))
        self._append_css_replacement(NagatoCssFont(self))

    def run(self):
        if self._enquiry("YUKI.N > args", "mini-mode"):
            NagatoMiniWindow(self)
        else:
            NagatoMainWindow(self)
