
from libnagato.config.CssReplacement import NagatoCssReplacement


class NagatoCssMainImage(NagatoCssReplacement):

    def _initialize_variables(self):
        self._query = "css", "background_image"
        self._target = "/*NAGATO_BACKGROUND_IMAGE_MAIN_WINDOW*/"
        self._template = "background-image: url('{}');"
        self._default = "images/main-window.png"
        self._path_check = True
