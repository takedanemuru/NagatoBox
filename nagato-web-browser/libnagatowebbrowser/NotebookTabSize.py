
from libnagato.Object import NagatoObject


class NagatoNotebookTabSize(NagatoObject):

    def _update(self):
        if self._count == 0:
            return
        yuki_width = int(self._width/self._count) - 16
        self._raise("YUKI.N > new tab size", yuki_width)

    def _on_check_tab_count(self,notebook, child, page_num):
        self._count = notebook.get_n_pages()
        self._update()

    def _on_configure_event(self, window, event):
        yuki_width, yuki_height = window.get_size()
        if self._width == yuki_width-64:
            return
        self._width = yuki_width-64
        self._update()

    def __init__(self, parent):
        self._parent = parent
        self._width = 0
        self._count = 1
        yuki_window = self._enquiry("YUKI.N > main window itself")
        yuki_window.connect("configure-event", self._on_configure_event)
        self._parent.connect("page-added", self._on_check_tab_count)
        self._parent.connect("page-removed", self._on_check_tab_count)
