
from pathlib import Path
from libnagato.Object import NagatoObject


class NagatoCssReplacement(NagatoObject):

    def replace(self, text):
        yuki_replacement = self._get_replacement()
        if yuki_replacement is None:
            yuki_url = self._template.format(self._default)
        else:
            yuki_url = self._template.format(yuki_replacement)
        return text.replace(self._target, yuki_url)

    def _get_replacement(self):
        yuki_path = self._enquiry("YUKI.N > config", self._query)
        if yuki_path == "":
            return None
        if self._path_check and not Path(yuki_path).exists():
            return None
        return yuki_path

    def _initialize_variables(self):
        self._query = "", ""
        self._target = ""
        self._template = ""
        self._default = ""
        self._path_check = True

    def __init__(self, parent):
        self._parent = parent
        self._initialize_variables()
