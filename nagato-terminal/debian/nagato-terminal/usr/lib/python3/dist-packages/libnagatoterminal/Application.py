
from libnagato.application.Application import NagatoApplication as TFEI
from libnagato.config.CssMainImage import NagatoCssMainImage
from libnagato.config.CssFont import NagatoCssFont
from libnagatoterminal.Window import NagatoWindow
from libnagato.dbus.Unique import NagatoUnique
from libnagatoterminal.dbus.RemoteObject import NagatoRemoteObject


class NagatoApplication(TFEI):

    def _initialize_css_replacements(self):
        self._append_css_replacement(NagatoCssMainImage(self))
        self._append_css_replacement(NagatoCssFont(self))

    def run(self):
        NagatoWindow(self)
