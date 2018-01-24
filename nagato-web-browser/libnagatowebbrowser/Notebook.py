
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.ui.NotebookTabVisibility import NagatoTabVisibility
from libnagatowebbrowser.PageContent import NagatoPageContent
from libnagatowebbrowser.NotebookTabSize import NagatoNotebookTabSize

DEFAULT_HOME_PAGE = "http://www.duckduckgo.com"


class NagatoNotebook(Gtk.Notebook, NagatoObject):

    def _yuki_n_create(self, uri=DEFAULT_HOME_PAGE):
        NagatoPageContent(self, uri)

    def _yuki_n_add_new_tab(self, uri=DEFAULT_HOME_PAGE):
        NagatoPageContent(self, uri)

    def _yuki_n_load_finished(self):
        self._raise_new_title(self.get_current_page())

    def _yuki_n_new_tab_size(self, new_tab_size):
        for yuki_child in self.get_children():
            yuki_child.set_tab_size(new_tab_size)
        self.show_all()

    def _inform_has_multi_tabs(self):
        return (self.get_n_pages() >= 2)

    def _raise_new_title(self, page_num):
        yuki_page = self.get_nth_page(page_num)
        self._raise("YUKI.N > new title", yuki_page.get_title())

    def _on_switch_page(self, notebook, page, page_num):
        if page_num >= 0:
            self._raise_new_title(page_num)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Notebook.__init__(self)
        self.set_scrollable(True)
        self.set_property("expand", True)
        self.set_property("resize-mode", Gtk.ResizeMode.QUEUE)
        NagatoTabVisibility(self)
        NagatoNotebookTabSize(self)
        self.connect("switch-page", self._on_switch_page)
        NagatoPageContent(self, DEFAULT_HOME_PAGE)
        self._parent.attach(self, 0, 2, 1, 1)
