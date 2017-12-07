
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal import GdkPixbufIcon
from libnagatoterminal.Settings import NagatoSettings


class NagatoWindowAttributes(NagatoObject):

    def _set_window_position(self, rect):
        self._parent.move(rect.left, rect.top)
        self._parent.set_default_size(rect.width, rect.height)

    def save_window_positions(self):
        yuki_width, yuki_height = self._parent.get_size()
        yuki_left, yuki_top = self._parent.get_position()
        self._settings.save_window_rect(
            yuki_left,
            yuki_top,
            yuki_width,
            yuki_height
            )

    def __init__(self, parent):
        self._parent = parent
        self._settings = NagatoSettings()
        self._parent.set_title("YUKI.N > ...")
        self._parent.set_icon(GdkPixbufIcon.get_application_icon())
        yuki_rect = self._settings.load_window_rect()
        if yuki_rect is not None:
            self._set_window_position(yuki_rect)
