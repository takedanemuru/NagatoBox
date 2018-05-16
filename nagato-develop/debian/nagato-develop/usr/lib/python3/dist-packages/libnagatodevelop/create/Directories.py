
import os
from pathlib import Path

DIRECTORIES = [
    "debian",
    "debian/source",
    "{}",
    "{}/Mikuru",
    "{}/eventbox",
    "{}/menu",
    "{}/menu/context",
    "{}/resources",
    "{}/resources/images",
    "{}/ui",
    "readme_extra"
    ]


class NagatoDirectories(object):

    def _get_path_object(self, sub_directory):
        return Path(os.path.join(self._data["app-directory"], sub_directory))

    def __init__(self, data):
        self._data = data
        for yuki_directory in DIRECTORIES:
            yuki_directory = yuki_directory.format(self._data["lib-name"])
            yuki_path = self._get_path_object(yuki_directory)
            yuki_path.mkdir(parents=True)
