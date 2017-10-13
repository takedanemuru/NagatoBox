
from gi.repository import Gtk
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.SourceView import NagatoSourceView


class NagatoNotebook(Gtk.Notebook, NagatoObject):

    def _on_order_changed(self, notebook, child, page_num):
        pass

    def _on_page_removed(self, notebook, child, page_num):
        pass

    def _on_switch_page(self, notebook, child, page_num):
        pass

    def _set_attributes(self):
        self.set_scrollable(True)
        self.set_property("expand", True)
        self.set_opacity(0.9)
        self.set_property("resize-mode", Gtk.ResizeMode.QUEUE)

    def _set_callbacks(self):
        self.connect("page-added", self._on_order_changed)
        self.connect("page-removed", self._on_page_removed)
        self.connect("page-reordered", self._on_order_changed)
        self.connect("switch-page", self._on_switch_page)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Notebook.__init__(self)
        self._set_attributes()
        self._parent.attach(self, 0, 2, 1, 1)
        self._set_callbacks()
        self._source_view = NagatoSourceView(self)
