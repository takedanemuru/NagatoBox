
import argparse
from libnagato.Object import NagatoObject
from libnagatodevelop.option.ShowVersion import NagatoShowVersion
from libnagatodevelop.option.LinesOfCode import NagatoLinesOfCode
from libnagatodevelop.option.Find import NagatoFind


class NagatoArgs(argparse.ArgumentParser, NagatoObject):

    def _get_args(self):
        NagatoShowVersion(self)
        NagatoFind(self)
        NagatoLinesOfCode(self)

    def _initialize_variants(self):
        yuki_args = self.parse_args()
        if yuki_args.find is not None:
            self._args["find"] = yuki_args.find[0]
        self._args["lines-of-code"] = yuki_args.lines_of_code
        self._args["show-version"] = yuki_args.show_version

    def __init__(self):
        argparse.ArgumentParser.__init__(self)
        self._args = {}
        self._get_args()
        self._initialize_variants()

    def __getitem__(self, key):
        if key in self._args:
            return self._args[key]
        else:
            return None
