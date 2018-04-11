
from pathlib import Path
from libnagato.Object import NagatoObject

MAIN_IMAGE = "/*NAGATO_BACKGROUND_IMAGE_MAIN_WINDOW*/"
TEMPLATE = "background-image: url('{}')"


class NagatoCssText(NagatoObject):

    def _get_default_text(self):
        yuki_source = self._enquiry("YUKI.N > resources", "application.css")
        return Path(yuki_source).read_text()

    def _replace_main_image(self, text):
        yuki_data = "css", "background_image"
        yuki_path = self._enquiry("YUKI.N > config", yuki_data)
        if yuki_path == "" or not Path(yuki_path).exists():
            yuki_url = TEMPLATE.format("images/main-window.png")
        else:
            yuki_url = TEMPLATE.format(yuki_path)
        return text.replace(MAIN_IMAGE, yuki_url)

    def get(self):
        yuki_text = self._get_default_text()
        yuki_text = self._replace_main_image(yuki_text)
        return yuki_text

    def __init__(self, parent):
        self._parent = parent
