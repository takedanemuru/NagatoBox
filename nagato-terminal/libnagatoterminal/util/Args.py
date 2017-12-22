
import argparse

from libnagatoterminal.util import Path


class NagatoArgs(object):

    _directory = ""
    _command = ""
    _show_version = False

    def _get_directory_option(self):
        self._parser.add_argument(
            "-d",
            nargs=1,
            metavar="DIRECTORY",
            help="set working directory")

    def _get_command_option(self):
        self._parser.add_argument(
            "-e",
            nargs=1,
            metavar="COMMAND",
            help="execute command")

    def _get_show_background_option(self):
        self._parser.add_argument(
            "-v",
            action="store_true",
            dest="show_version",
            default=False,
            help="show version")

    def _get_args(self):
        self._get_directory_option()
        self._get_command_option()
        self._get_show_background_option()

    def _get_directory(self, args):
        if args.d is not None:
            return args.d[0]
        return Path.get_home()

    def _initialize_variants(self):
        yuki_args = self._parser.parse_args()
        NagatoArgs._directory = self._get_directory(yuki_args)
        NagatoArgs._command = yuki_args.e[0] if yuki_args.e else None
        NagatoArgs._show_version = yuki_args.show_version

    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._get_args()
        self._initialize_variants()

    def get_vte_directory(self, is_prime_vte):
        if is_prime_vte:
            return NagatoArgs._directory
        else:
            return Path.get_home()

    @property
    def directory(self):
        return NagatoArgs._directory

    @property
    def command(self):
        return NagatoArgs._command

    @property
    def show_version(self):
        return NagatoArgs._show_version
