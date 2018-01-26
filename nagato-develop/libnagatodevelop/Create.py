
import os
import shutil
from gi.repository import GLib
from pathlib import Path

DIRECTORIES = [
    "", 
    "debian",
    "debian/source",
    "libnagatopowered",
    "libnagatopowered/dialog",
    "libnagatopowered/dialog/label",
    "libnagatopowered/eventbox",
    "libnagatopowered/menu",
    "libnagatopowered/menu/context",
    "libnagatopowered/resources",
    "libnagatopowered/resources/images",
    "readme_extra"
    ]


class NagatoCreate(object):

    def _create_directories(self, target_directory):
        for yuki_directory in DIRECTORIES:
            yuki_path = Path(os.path.join(target_directory, yuki_directory))
            yuki_path.mkdir(parents=True)

    def _get_target_path(self, source_path):
        yuki_target = source_path.replace("libAPPNAME", "libnagatopowered")
        yuki_target = yuki_target.replace(
            self._template_directory,
            self._target_directory)
        yuki_target = yuki_target.replace("APPNAME", "nagato-powered")
        return yuki_target

    def _replacing_copy(self, source_path, target_path):
        yuki_text = Path(source_path).read_text()
        yuki_text = yuki_text.replace("libAPPNAME", "libnagatopowered")
        yuki_text = yuki_text.replace("APPNAME", "nagato-powered")
        yuki_text = yuki_text.replace("AUTHOR_NAME", "takeda.nemuru")
        yuki_text = yuki_text.replace(
            "AUTHOR_EMAIL",
            "<takeda.nemuru@yandex.com>"
            )
        Path(target_path).write_text(yuki_text)

    def _copy_files(self, template_directory):
        for yuki_path in Path(template_directory).glob("**/*"):
            yuki_source_path = str(yuki_path)
            yuki_target_path = self._get_target_path(yuki_source_path)
            if yuki_path.is_dir():
                continue
            if yuki_source_path.endswith("png")\
            or yuki_source_path.endswith("jpg"):
                shutil.copy2(yuki_source_path, yuki_target_path)
            else:
                self._replacing_copy(yuki_source_path, yuki_target_path)

    def Create(self, template_directory):
        self._template_directory = template_directory
        self._target_directory = os.path.join(
            os.path.join(os.environ["HOME"], "working_dir"),
            "nagato-powered"
            )
        self._create_directories(self._target_directory)
        self._copy_files(template_directory)
        print("done in : ", self._target_directory)

    def __init__(self):
        pass
