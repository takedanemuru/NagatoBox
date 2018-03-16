
import argparse


class NagatoArgs(argparse.ArgumentParser):

    def _set_focus(self):
        self.add_argument(
            "-f",
            "--focus",
            action="store_true",
            dest="focus",
            default=False,
            help="focused window only"
            )

    def _set_delay(self):
        self.add_argument(
            "-d",
            "--delay",
            dest="delay",
            type=int,
            default=0,
            metavar="SECONDS",
            help="set delay in seconds"
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
        self._set_delay()
        self._set_focus()
        self._set_show_version()

    def _initialize_variants(self):
        yuki_args = self.parse_args()
        self._args = {}
        self._args["show-version"] = yuki_args.show_version
        self._args["focus"] = yuki_args.focus
        self._args["delay"] = max(0, yuki_args.delay)

    def __init__(self):
        argparse.ArgumentParser.__init__(self)
        self._get_args()
        self._initialize_variants()

    def __getitem__(self, key):
        return self._args[key]
