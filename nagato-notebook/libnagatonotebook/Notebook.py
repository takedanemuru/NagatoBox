
from gi.repository import Gtk
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.ScrolledWindow import NagatoScrolledWindow
from libnagatonotebook.DialogSaveFile import NagatoDialogSaveFile


class NagatoNotebook(Gtk.Notebook, NagatoObject):

    def _on_order_changed(self, notebook, child, page_num):
        self.set_show_tabs(self.get_n_pages() > 1)

    def _on_page_removed(self, notebook, child, page_num):
        pass

    def _on_switch_page(self, notebook, child, page_num):
        pass

    def _set_attributes(self):
        self.set_scrollable(True)
        self.set_property("hexpand", True)
        self.set_property("vexpand", True)
        self.set_opacity(0.9)

    def _set_callbacks(self):
        self.connect("page-added", self._on_order_changed)
        self.connect("page-reordered", self._on_order_changed)
        self.connect("page-removed", self._on_page_removed)
        self.connect("switch-page", self._on_switch_page)

    def _get_active_source_view(self):
        yuki_current_page = self.get_current_page()
        return self.get_nth_page(yuki_current_page)

    def new(self):
        NagatoScrolledWindow(self)
        self.show_all()

    def file_open(self):
        yuki_dialog = NagatoDialogSaveFile()
        yuki_path, yuki_response = yuki_dialog.open_file()
        if yuki_response == Gtk.ResponseType.APPLY:
            NagatoScrolledWindow(self, yuki_path)
            self.show_all()

    def save(self):
        self._get_active_source_view().save()

    def save_as(self):
        self._get_active_source_view().save_as()

    def __init__(self, parent):
        self._parent = parent
        Gtk.Notebook.__init__(self)
        self._set_attributes()
        self._parent.attach(self, 0, 2, 1, 1)
        self._set_callbacks()
        NagatoScrolledWindow(self)
        self.show_all()
