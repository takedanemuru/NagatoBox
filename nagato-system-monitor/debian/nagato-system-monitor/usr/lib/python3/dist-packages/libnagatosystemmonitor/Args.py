
import argparse


class NagatoArgs(argparse.ArgumentParser):

    def _set_show_version(self):
        self.add_argument(
            "-v",
            "--version",
            action="store_true",
            dest="show_version",
            default=False,
            help="show version"
            )

    def _get_args(self):
        self._set_show_version()

    def _initialize_variants(self):
        yuki_args = self.parse_args()
        self._args = {}
        self._args["show-version"] = yuki_args.show_version

    def __init__(self):
        argparse.ArgumentParser.__init__(self)
        self._get_args()
        self._initialize_variants()

    def __getitem__(self, key):
        return self._args[key]
