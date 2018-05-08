
from libnagato.config.CssReplacement import NagatoCssReplacement


class NagatoCssFont(NagatoCssReplacement):

    def _initialize_variables(self):
        self._query = "css", "font"
        self._target = "/*NAGATO_FONT*/"
        self._template = "font: {};"
        self._default = "Ubuntu Mono Regular 14"
        self._path_check = False
