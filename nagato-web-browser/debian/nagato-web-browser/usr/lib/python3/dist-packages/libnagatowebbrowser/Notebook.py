

from gi.repository import Gtk
from libnagatowebbrowser.CoreObject import NagatoObject
from libnagatowebbrowser.WebView import NagatoWebView

DEFAULT_HOME_PAGE = "http://www.duckduckgo.com"


class NagatoNotebook(Gtk.Notebook, NagatoObject):

    def _yuki_n_create(self, user_data):
        NagatoWebView(self, user_data)
        self.show_all()

    def _yuki_n_load_finished(self, user_data):
        if user_data == self.get_current_page():
            self._on_raise_current_page_load_finished()

    def _on_order_changed(self, notebook, child, page_num):
        self._reorder_pages()

    def _on_page_removed(self, notebook, child, page_num):
        self._reorder_pages()
        if self.get_current_page() >= page_num:
            self._on_raise_current_page_load_finished()

    def _on_switch_page(self, notebook, child, page_num):
        if self.get_current_page() >= 0:
            self._on_raise_current_page_load_finished(page_num)

    def _on_raise_current_page_load_finished(self, page_num=None):
        if page_num is None:
            page_num = self.get_current_page()
        yuki_web_view = self.get_nth_page(page_num)
        yuki_page_data = yuki_web_view.page_data
        self._raise("YUKI.N > current page load finished", yuki_page_data)

    def _reorder_pages(self):
        for yuki_page_index in range(self.get_n_pages()):
            yuki_web_view = self.get_nth_page(yuki_page_index)
            yuki_web_view.set_position(yuki_page_index)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Notebook.__init__(self)
        self.set_scrollable(True)
        self.set_property("expand", True)
        self._parent.attach(self, 0, 2, 1, 1)
        self.set_opacity(0.9)
        self.connect("page-added", self._on_order_changed)
        self.connect("page-removed", self._on_page_removed)
        self.connect("page-reordered", self._on_order_changed)
        self.connect("switch-page", self._on_switch_page)
        NagatoWebView(self, DEFAULT_HOME_PAGE)
