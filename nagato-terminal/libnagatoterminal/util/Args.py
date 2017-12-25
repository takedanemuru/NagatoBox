
import argparse
import os


class NagatoArgs(object):

    def _get_directory_option(self):
        self._parser.add_argument(
            "-d",
            nargs=1,
            metavar="DIRECTORY",
            help="set working directory"
            )

    def _get_command_option(self):
        self._parser.add_argument(
            "-e",
            nargs=1,
            metavar="COMMAND",
            help="execute command"
            )

    def _get_show_version(self):
        self._parser.add_argument(
            "-v",
            "--version",
            action="store_true",
            dest="show_version",
            default=False,
            help="show version"
            )

    def _get_args(self):
        self._get_directory_option()
        self._get_command_option()
        self._get_show_version()

    def _get_directory(self, args):
        if args.d is not None:
            return args.d[0]
        return os.environ["HOME"]

    def _initialize_variants(self):
        yuki_args = self._parser.parse_args()
        NagatoArgs._directory = self._get_directory(yuki_args)
        NagatoArgs._command = yuki_args.e[0] if yuki_args.e else None
        NagatoArgs._show_version = yuki_args.show_version

    def __init__(self):
        if "_command" in NagatoArgs.__dict__.keys():
            return
        self._parser = argparse.ArgumentParser()
        self._get_args()
        self._initialize_variants()

    def get_vte_directory(self, is_prime_vte):
        if is_prime_vte:
            return NagatoArgs._directory
        else:
            return os.environ["HOME"]

    @property
    def directory(self):
        return NagatoArgs._directory

    @property
    def command(self):
        return NagatoArgs._command

    @property
    def show_version(self):
        return NagatoArgs._show_version
