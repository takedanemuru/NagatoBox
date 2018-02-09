
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from libnagato.Object import NagatoObject
from libnagatogifviewer.eventbox.ForLabel import NagatoEventBox
from libnagatogifviewer.Resources import NagatoResources

GRID_SPACING = 16


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_border_width(GRID_SPACING)
        self.set_row_spacing(GRID_SPACING)
        self.set_column_spacing(GRID_SPACING)

    def _add_gtk_image(self):
        yuki_resources = NagatoResources()
        yuki_path = yuki_resources.get_image_path("doublas.gif")
        yuki_animation = GdkPixbuf.PixbufAnimation.new_from_file(yuki_path)
        self._gtk_image = Gtk.Image.new_from_animation(yuki_animation)

    def __init__(self, parent):
        self._parent = parent
        self._initialize_grid()
        self._parent.add(self)
        self._add_gtk_image()
        self.attach(NagatoEventBox(self), 0, 0, 1, 1)
        self.attach(self._gtk_image, 0, 1, 1, 1)
