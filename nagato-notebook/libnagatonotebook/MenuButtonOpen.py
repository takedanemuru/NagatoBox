
from libnagatonotebook.MenuButton import NagatoMenuButton


class NagatoMenuButtonOpen(NagatoMenuButton):

    def _initialize_variants(self):
        self._icon_name = "document-open-symbolic"
        self._tooltip_text = "open file"
        self._message = "YUKI.N > file open"
