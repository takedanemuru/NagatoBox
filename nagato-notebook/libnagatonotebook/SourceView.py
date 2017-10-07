
import gi

gi.require_version("GtkSource", "3.0")

from gi.repository import GtkSource
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.UserInput import NagatoUserInput
from libnagatonotebook.File import NagatoFile

class NagatoSourceView(GtkSource.View, NagatoObject):

    def save(self):
        self._file.save()

    def _set_attributes(self):
        self.set_opacity(0.9)
        self.set_hexpand(True)
        self.set_vexpand(True)

    def __init__(self, parent):
        self._parent = parent
        GtkSource.View.__init__(self)
        #NagatoUserInput(self)
        self._file = NagatoFile(self)
        self._set_attributes()
        self._parent.attach(self, 0, 1, 1, 1)
        self.grab_focus()
