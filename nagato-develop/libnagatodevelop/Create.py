
import os
import shutil
from gi.repository import GLib
from pathlib import Path
from libnagatodevelop.create.Directories import NagatoDirectories
from libnagatodevelop.create.Files import NagatoFiles


APPNAME = "nagato-develop"
LIBNAME = "lib"+APPNAME.replace("-", "")
APP_ID = "io.github.takedanemuru.{}".format(APPNAME)
APP_WEBSITE = "https://takedanemuru.github.io"
AUTHOR_NAME = "takeda.nemuru"
AUTHOR_EMAIL = "<takeda.nemuru@yandex.com>"
WORKING_DIRECTORY = os.path.join(os.environ["HOME"], "working_dir")
SHORT_DESCRIPTION = "powered by nagato"
COPYRIGHT_YEAR = "2018"
COPYRIGHT_MONTH = "January"


class NagatoCreate(object):

    def _get_target_path(self, source_path):
        yuki_target = source_path.replace("APP_ID", APP_ID)
        yuki_target = yuki_target.replace("libAPPNAME", LIBNAME)
        yuki_target = yuki_target.replace(
            self._template_directory,
            self._target_directory)
        yuki_target = yuki_target.replace("APPNAME", APPNAME)
        return yuki_target

    def _replacing_copy(self, source_path, target_path):
        yuki_text = Path(source_path).read_text()
        yuki_text = yuki_text.replace("libAPPNAME", LIBNAME)
        yuki_text = yuki_text.replace("APPNAME", APPNAME)
        yuki_text = yuki_text.replace("APP_ID", APP_ID)
        yuki_text = yuki_text.replace("APP_WEBSITE", APP_WEBSITE)
        yuki_text = yuki_text.replace("AUTHOR_NAME", AUTHOR_NAME)
        yuki_text = yuki_text.replace("AUTHOR_EMAIL", AUTHOR_EMAIL)
        yuki_text = yuki_text.replace("COPYRIGHT_YEAR", COPYRIGHT_YEAR)
        yuki_text = yuki_text.replace("COPYRIGHT_MONTH", COPYRIGHT_MONTH)
        yuki_text = yuki_text.replace("SHORT_DESCRIPTION", SHORT_DESCRIPTION)
        Path(target_path).write_text(yuki_text)

    def _copy_file(self, source_path):
        yuki_source_path = source_path
        yuki_target_path = self._get_target_path(yuki_source_path)
        if yuki_source_path.endswith(".pyc"):
            return
        if yuki_source_path.endswith(".png")\
        or yuki_source_path.endswith(".jpg"):
            shutil.copy2(yuki_source_path, yuki_target_path)
        else:
            self._replacing_copy(yuki_source_path, yuki_target_path)

    def _copy_files(self, template_directory):
        for yuki_path in Path(template_directory).glob("**/*"):
            if yuki_path.is_dir():
                continue
            self._copy_file(str(yuki_path))

    def Create(self, template_directory):
        self._template_directory = template_directory
        self._target_directory = os.path.join(WORKING_DIRECTORY, APPNAME)
        self._directories = NagatoDirectories()
        self._directories.initialize(LIBNAME, self._target_directory)
        self._copy_files(template_directory)
        print("done in : ", self._target_directory)

    def __init__(self):
        pass
