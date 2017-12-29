
import os
import argparse


class NagatoArgs(argparse.ArgumentParser):

    def _add_argument(self, arg_short, count, metavar_name, help_text):
        self.add_argument(
            arg_short,
            nargs=count,
            metavar=metavar_name,
            help=help_text
            )

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
        self._add_argument("-e", 1, "COMMAND", "execute command")
        self._add_argument("-d", 1, "DIRECTORY", "set working directory")
        self._set_show_version()

    def _get_directory(self, args):
        if args.d is not None:
            return args.d[0]
        return os.environ["HOME"]

    def _initialize_variants(self):
        yuki_args = self.parse_args()
        self._args = {}
        self._args["directory"] = self._get_directory(yuki_args)
        self._args["command"] = yuki_args.e[0] if yuki_args.e else None
        self._args["show-version"] = yuki_args.show_version

    def __init__(self):
        argparse.ArgumentParser.__init__(self)
        self._get_args()
        self._initialize_variants()

    def __getitem__(self, key):
        return self._args[key]
