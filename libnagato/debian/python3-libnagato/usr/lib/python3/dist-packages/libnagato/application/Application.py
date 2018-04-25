
from libnagato.Object import NagatoObject
from libnagato.application.Resources import ShamisenResources
from libnagato.application.Config import ShamisenConfig
from libnagato.config.Resources import NagatoResources
from libnagato.config.Config import NagatoConfig
from libnagato.config.Css import NagatoCss


class NagatoApplication(NagatoObject, ShamisenConfig, ShamisenResources):

    def _inform_css_replacements(self):
        return self._css_replacements

    def _append_css_replacement(self, css_replacement):
        self._css_replacements.append(css_replacement)

    def _initialize_css_replacements(self):
        pass

    def __init__(self, parent):
        self._parent = parent
        self._resources = NagatoResources(self)
        self._config = NagatoConfig(self)
        self._css_replacements = []
        self._initialize_css_replacements()
        self._css = NagatoCss(self)
