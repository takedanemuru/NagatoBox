
from gi.repository import Gtk
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.TabLabel import NagatoTabLabel
from libnagatonotebook.SourceView import NagatoSourceView


class NagatoScrolledWindow(Gtk.ScrolledWindow, NagatoObject):

    def save(self):
        self._source_view.save()

    def save_as(self):
        self._source_view.save_as()

    def _setup_page(self):
        self._tab_label = NagatoTabLabel(self)
        self._page_index = self._parent.insert_page(
            self,
            self._tab_label,
            -1
            )
        self._parent.set_tab_reorderable(self, True)

    def __init__(self, parent, path_to_file=None):
        self._parent = parent
        Gtk.ScrolledWindow.__init__(self)
        self.set_policy(
            Gtk.PolicyType.AUTOMATIC,
            Gtk.PolicyType.AUTOMATIC
            )
        self._source_view = NagatoSourceView(self, path_to_file)
        self.add(self._source_view)
        self._setup_page()
