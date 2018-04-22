
from libnagato.Object import NagatoObject
from libnagatotext.Resources import NagatoResources
from libnagatotext.Config import NagatoConfig
from libnagatotext.application.Resources import ShamisenResources
from libnagatotext.application.Config import ShamisenConfig


class NagatoApplication(NagatoObject, ShamisenConfig, ShamisenResources):

    def _inform_css_replacements(self):
        return self._css_replacements

    def _initialize_css_replacements(self):
        pass

    def __init__(self, parent):
        self._parent = parent
        self._resources = NagatoResources(self)
        self._config = NagatoConfig(self)
        self._css_replacements = []
        self._initialize_css_replacements()
