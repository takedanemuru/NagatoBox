
import shutil
import datetime
from pathlib import Path


class NagatoFiles(object):

    def _get_target_path(self, source_path):
        yuki_target = source_path.replace("APP_ID", self._data["app-id"])
        yuki_target = yuki_target.replace("libAPPNAME", self._data["lib-name"])
        yuki_target = yuki_target.replace(
            self._prototype_directory,
            self._data["app-directory"])
        yuki_target = yuki_target.replace("APPNAME", self._data["app-name"])
        return yuki_target

    def _replacing_copy(self, source_path, target_path):
        yuki_now = datetime.datetime.now()
        yuki_text = Path(source_path).read_text()
        yuki_text = yuki_text.replace("libAPPNAME", self._data["lib-name"])
        yuki_text = yuki_text.replace("APPNAME", self._data["app-name"])
        yuki_text = yuki_text.replace("APP_ID", self._data["app-id"])
        yuki_text = yuki_text.replace("APP_WEBSITE", self._data["app-uri"])
        yuki_text = yuki_text.replace("AUTHOR_NAME", self._data["user-name"])
        yuki_text = yuki_text.replace("AUTHOR_EMAIL", self._data["user-email"])
        yuki_text = yuki_text.replace("COPYRIGHT_YEAR", str(yuki_now.year))
        yuki_text = yuki_text.replace("COPYRIGHT_MONTH", str(yuki_now.month))
        yuki_text = yuki_text.replace(
            "SHORT_DESCRIPTION",
            self._data["app-short-description"]
            )
        Path(target_path).write_text(yuki_text)

    def _ensure_file(self, source_path):
        yuki_source_path = source_path
        yuki_target_path = self._get_target_path(yuki_source_path)
        if yuki_source_path.endswith(".pyc"):
            return
        if yuki_source_path.endswith(".png"):
            shutil.copy2(yuki_source_path, yuki_target_path)
        else:
            self._replacing_copy(yuki_source_path, yuki_target_path)

    def _ensure_files(self):
        for yuki_path in Path(self._prototype_directory).glob("**/*"):
            if yuki_path.is_dir():
                continue
            self._ensure_file(str(yuki_path))

    def __init__(self, data, prototype_directory):
        self._data = data
        self._prototype_directory = prototype_directory
        self._ensure_files()
