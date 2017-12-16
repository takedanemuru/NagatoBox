

class NagatoTabVisibility(object):

    def _on_order_changed(self, notebook, child, page_num):
        self._parent.set_show_tabs(self._parent.get_n_pages() > 1)

    def _set_callbacks(self):
        self._parent.connect("page-added", self._on_order_changed)
        self._parent.connect("page-reordered", self._on_order_changed)
        self._parent.connect("page-removed", self._on_order_changed)

    def __init__(self, parent):
        self._parent = parent
        self._set_callbacks()
