
import os
from pathlib import Path


class NagatoLongDescription(object):

    def _get_control_path(self):
        yuki_path = os.path.join(
            self._data["app-directory"],
            "debian/control"
            )
        return yuki_path

    def _get_yml_path(self):
        yuki_path = os.path.join(
            self._data["app-directory"],
            self._data["lib-name"],
            "resources/application.yaml"
            )
        return yuki_path

    def _get_text_to_replace(self, head):
        yuki_out = ""
        for yuki_line in self._data["app-long-description"].split("\n"):
            if yuki_line != "":
                yuki_out += head+yuki_line+"\n"
        return yuki_out

    def _replace_control(self):
        yuki_path = self._get_control_path()
        yuki_replacement = self._get_text_to_replace(" ")
        yuki_source = Path(yuki_path).read_text()
        yuki_source = yuki_source.replace(
            " LONG_DESCRIPTION",
            yuki_replacement
            )
        Path(yuki_path).write_text(yuki_source)

    def _replace_application_yaml(self):
        yuki_path = self._get_yml_path()
        yuki_replacement = self._get_text_to_replace("    ")
        yuki_source = Path(yuki_path).read_text()
        yuki_source = yuki_source.replace(
            "    LONG_DESCRIPTION",
            yuki_replacement
            )
        Path(yuki_path).write_text(yuki_source)

    def __init__(self, data):
        self._data = data
        self._replace_control()
        self._replace_application_yaml()
