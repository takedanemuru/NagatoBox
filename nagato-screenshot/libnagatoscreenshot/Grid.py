
import os
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatoscreenshot.Preview import NagatoPreview
from libnagatoscreenshot.pathentry.ForFile import NagatoPathEntry as ForFile
from libnagatoscreenshot.pathentry.ForDir import NagatoPathEntry as ForDir
from libnagatoscreenshot.ActionButton import NagatoActionButton
from libnagatoscreenshot.dialog.SuccessfullySaved import NagatoSaved

GRID_SPACING = 16


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _yuki_n_dir_name_changed(self, path):
        self._dir_name = path

    def _yuki_n_file_name_changed(self, path):
        self._file_name = path

    def _yuki_n_save(self):
        yuki_path = os.path.join(self._dir_name, self._file_name)
        self._raise("YUKI.N > save to", yuki_path)
        NagatoSaved.call(yuki_path)
        self._raise("YUKI.N > quit")

    def _initialize_contents(self):
        self.attach(NagatoPreview(self), 0, 0, 3, 4)
        yuki_for_file = ForFile(self, 3, 0)
        yuki_for_dir = ForDir(self, 3, 1)
        yuki_spacer = Gtk.Label("")
        yuki_spacer.set_vexpand(True)
        self.attach(yuki_spacer, 3, 3, 3, 1)
        self.attach(Gtk.Separator.new(Gtk.Orientation.HORIZONTAL), 0, 4, 6, 1)
        NagatoActionButton(self, 4, 5, "Cancel", "YUKI.N > quit")
        NagatoActionButton(self, 5, 5, "Save", "YUKI.N > save", "SaveButton")

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_column_homogeneous(True)
        self.set_row_homogeneous(False)
        self.set_border_width(GRID_SPACING)
        self.set_row_spacing(GRID_SPACING)
        self.set_column_spacing(GRID_SPACING)

    def __init__(self, parent):
        self._parent = parent
        self._initialize_grid()
        self._parent.add(self)
        self._initialize_contents()
