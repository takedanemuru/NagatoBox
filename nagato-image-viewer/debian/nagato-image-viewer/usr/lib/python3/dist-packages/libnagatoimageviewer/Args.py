
import argparse
from libnagatoimageviewer.Mikuru import Options
from libnagatoimageviewer.Mikuru import PathSanitizer

MIME = "image"


class NagatoArgs(argparse.ArgumentParser):

    def _get_args(self):
        self.add_argument("-v", "--version", **Options.SHOW_VERSION)
        self.add_argument("path", **Options.FILE_PATH)

    def _initialize_variants(self):
        yuki_args = self.parse_args()
        self._args = {}
        self._args["show-version"] = yuki_args.show_version
        self._args["path"] = PathSanitizer.get_a_path(yuki_args.path, MIME)

    def __init__(self):
        argparse.ArgumentParser.__init__(self)
        self._get_args()
        self._initialize_variants()

    def __getitem__(self, key):
        return self._args[key]
