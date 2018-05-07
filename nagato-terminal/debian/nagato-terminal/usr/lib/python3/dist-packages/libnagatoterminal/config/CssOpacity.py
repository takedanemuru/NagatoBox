
from libnagato.config.CssReplacement import NagatoCssReplacement


class NagatoCssOpacity(NagatoCssReplacement):

    def _initialize_variables(self):
        self._query = "css", "opacity"
        self._target = "/*NAGATO_OPACITY*/"
        self._template = "opacity: {};"
        self._default = "0.7"
        self._path_check = False
