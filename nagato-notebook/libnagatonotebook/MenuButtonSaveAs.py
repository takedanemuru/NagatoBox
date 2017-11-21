
from libnagatonotebook.MenuButton import NagatoMenuButton


class NagatoMenuButtonSaveAs(NagatoMenuButton):

    def _initialize_variants(self):
        self._icon_name = "document-save-as-symbolic"
        self._tooltip_text = "save as ..."
        self._message = "YUKI.N > file save as"
