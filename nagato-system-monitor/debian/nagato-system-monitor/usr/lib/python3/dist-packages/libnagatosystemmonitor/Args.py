
import argparse
from libnagatosystemmonitor.Mikuru import Options


class NagatoArgs(argparse.ArgumentParser):

    def _get_args(self):
        self.add_argument("-v", "--version", **Options.SHOW_VERSION)
        self.add_argument("-m", "--mini-mode", **Options.MINI_MODE)

    def _initialize_variants(self):
        yuki_args = self.parse_args()
        self._args = {}
        self._args["show-version"] = yuki_args.show_version
        self._args["mini-mode"] = yuki_args.mini_mode

    def __init__(self):
        argparse.ArgumentParser.__init__(self)
        self._get_args()
        self._initialize_variants()

    def __getitem__(self, key):
        return self._args[key]
