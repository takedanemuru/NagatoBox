
from pathlib import Path
from libnagato.Object import NagatoObject


class NagatoCssReplacement(NagatoObject):

    def replace(self, text):
        yuki_replacement = self._get_replacement()
        yuki_new = self._template.format(yuki_replacement)
        return text.replace(self._target, yuki_new)

    def _get_replacement(self):
        yuki_replacement = self._enquiry("YUKI.N > config", self._query)
        if yuki_replacement == "":
            return self._default
        if self._path_check and not Path(yuki_replacement).exists():
            return self._default
        return yuki_replacement

    def _initialize_variables(self):
        self._query = "", ""
        self._target = ""
        self._template = ""
        self._default = ""
        self._path_check = True

    def __init__(self, parent):
        self._parent = parent
        self._initialize_variables()
