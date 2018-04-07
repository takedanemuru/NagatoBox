
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatodevelop.group.Author import NagatoAuthor
from libnagatodevelop.group.Application import NagatoApplication
from libnagatodevelop.group.Description import NagatoDescription

GRID_SPACING = 16


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _switch(self, group):
        yuki_child = self.get_child_at(0, 0)
        yuki_child.destroy()
        self.attach(group, 0, 0, 1, 1)
        self.show_all()

    def _yuki_n_go_to_application(self):
        self._switch(NagatoApplication(self))

    def _yuki_n_go_to_author(self):
        self._switch(NagatoAuthor(self))

    def _yuki_n_go_to_description(self):
        self._switch(NagatoDescription(self))

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_border_width(GRID_SPACING)
        self.set_row_spacing(0)
        self.set_column_spacing(0)

    def __init__(self, parent):
        self._parent = parent
        self._initialize_grid()
        self._parent.add(self)
        self.attach(NagatoAuthor(self), 0, 0, 1, 1)
