
from libnagatonotebook.MenuButton import NagatoMenuButton


class NagatoMenuButtonNew(NagatoMenuButton):

    def _initialize_variants(self):
        self._icon_name = "document-new-symbolic"
        self._tooltip_text = "new"
        self._message = "YUKI.N > file new"
