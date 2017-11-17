
import gi

gi.require_version("GtkSource", "3.0")

from gi.repository import GtkSource
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.UserInput import NagatoUserInput
from libnagatonotebook.File import NagatoFile
from libnagatonotebook.TabLabel import NagatoTabLabel


class NagatoSourceView(GtkSource.View, NagatoObject):

    def save(self):
        self._file.save()

    def save_as(self):
        self._file.save_as()

    def _set_attributes(self):
        self.set_opacity(0.9)
        self.set_hexpand(True)
        self.set_vexpand(True)

    def _setup_tab(self):
        self._tab_label = NagatoTabLabel(self)
        self._page_index = self._parent.insert_page(self, self._tab_label, -1)
        self._parent.set_tab_reorderable(self, True)
        self._parent.set_show_tabs(self._parent.get_n_pages() > 1)

    def __init__(self, parent, path_to_file=None):
        self._parent = parent
        GtkSource.View.__init__(self)
        #NagatoUserInput(self)
        self._file = NagatoFile(self)
        self._set_attributes()
        self._setup_tab()
        self.grab_focus()
        self.set_highlight_current_line(True)
        if path_to_file != None:
            self._file.set_file(path_to_file)
