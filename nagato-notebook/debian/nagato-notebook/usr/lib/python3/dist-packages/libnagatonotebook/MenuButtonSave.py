
from libnagatonotebook.MenuButton import NagatoMenuButton


class NagatoMenuButtonSave(NagatoMenuButton):

    def _initialize_variants(self):
        self._icon_name = "document-save-symbolic"
        self._tooltip_text = "save"
        self._message = "YUKI.N > file save"
