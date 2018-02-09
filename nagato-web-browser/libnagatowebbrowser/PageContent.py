
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatowebbrowser.NotebookTab import NagatoNotebookTab
from libnagatowebbrowser.WebViewX import NagatoWebView
from libnagatowebbrowser.InPageSearch import NagatoInPageSearch


class NagatoPageContent(Gtk.Box, NagatoObject):

    def _yuki_n_close_current_tab(self):
        self._parent.detach_tab(self)
        self._tab_label.destroy()
        self.destroy()

    def _yuki_n_load_finished(self, title=None):
        if title is not None:
            self._tab_label.set_title(title)
            self._raise("YUKI.N > load finished")

    def _yuki_n_load_changed(self, progress):
        print(self.get_title(), progress)
        self._tab_label.set_progress(progress)

    def _setup_tab(self):
        self._tab_label = NagatoNotebookTab(self)
        yuki_page = self._parent.get_current_page()
        self._parent.insert_page(self, self._tab_label, yuki_page+1)
        self._parent.set_tab_reorderable(self, True)

    def __init__(self, parent, uri):
        self._parent = parent
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.set_homogeneous(False)
        self._web_view = NagatoWebView(self, uri)
        self._setup_tab()

    def get_title(self):
        self._web_view.get_title()

    def set_tab_size(self, new_tab_size):
        self._tab_label.set_tab_size(new_tab_size)
