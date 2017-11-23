
import gi

gi.require_version("GtkSource", "3.0")

from gi.repository import GtkSource
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.File import NagatoFile
#from libnagatonotebook.UserInput import NagatoUserInput


class NagatoSourceView(GtkSource.View, NagatoObject):

    def _set_attributes(self):
        self.set_opacity(0.9)
        self.set_hexpand(True)
        self.set_vexpand(True)
        self.set_show_line_numbers(True)
        self.set_highlight_current_line(True)

    def save(self):
        self._file.save()

    def save_as(self):
        self._file.save_as()

    def __init__(self, parent, path_to_file=None):
        self._parent = parent
        GtkSource.View.__init__(self)
        self._file = NagatoFile(self)
        self._set_attributes()
        self.grab_focus()
        if path_to_file is not None:
            self._file.set_file(path_to_file)
