
import os
from libnagatodevelop.IconImage import NagatoIconImage


class NagatoIcons(object):

    def _get_path_for_entry(self):
        yuki_path = os.path.join(
            self._data["app-directory"],
            "{}.png".format(self._data["app-id"])
            )
        return yuki_path

    def _get_path_for_resources(self):
        yuki_path = os.path.join(
            self._data["app-directory"],
            "{}/resources/application.png".format(self._data["lib-name"])
            )
        return yuki_path

    def _ensure(self):
        yuki_icon = NagatoIconImage(self._data["app-icon"])
        yuki_icon.save_to(self._get_path_for_entry())
        yuki_icon.save_to(self._get_path_for_resources())

    def __init__(self, data):
        self._data = data
        self._ensure()
