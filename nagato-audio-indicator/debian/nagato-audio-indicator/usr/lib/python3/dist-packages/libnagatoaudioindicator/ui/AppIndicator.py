
from gi.repository import Gtk
from gi.repository import AppIndicator3
from libnagato.Object import NagatoObject
from libnagatoaudioindicator.AlsaMixer import NagatoAlsaMixer
from libnagatoaudioindicator.menu.ForAppIndicator import NagatoMenu


class NagatoAppIndicator(NagatoObject):

    def _yuki_n_range(self, volume_range):
        self._alsa_mixer.set_volume(volume_range)

    def _inform_volume(self):
        return self._alsa_mixer.volume

    def _yuki_n_quit(self):
        Gtk.main_quit()

    def _initialize_app_indicator(self):
        self._indicator = AppIndicator3.Indicator.new(
            self._enquiry("YUKI.N > data", "id"),
            "audio-volume-high",
            AppIndicator3.IndicatorCategory.HARDWARE
            )
        self._indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self._indicator.set_menu(NagatoMenu(self))

    def __init__(self, parent):
        self._parent = parent
        self._alsa_mixer = NagatoAlsaMixer(self)
        self._initialize_app_indicator()
        Gtk.main()
