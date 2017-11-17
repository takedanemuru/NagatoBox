
from gi.repository import Gtk
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.BoxToolbar import NagatoBoxToolbar
from libnagatonotebook.Notebook import NagatoNotebook


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _yuki_n_file_save(self):
        self._notebook.save()

    def _yuki_n_file_save_as(self):
        self._notebook.save_as()

    def _yuki_n_file_new(self):
        self._notebook.new()

    def _yuki_n_file_open(self):
        self._notebook.file_open()

    def __init__(self, parent):
        self._parent = parent
        Gtk.Grid.__init__(self)
        self._parent.add(self)
        self.set_border_width(16)
        self.set_row_spacing(16)
        self.set_hexpand(True)
        self.set_vexpand(True)
        self._toolbar = NagatoBoxToolbar(self)
        self._notebook = NagatoNotebook(self)
        self.show_all()
