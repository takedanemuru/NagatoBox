
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.Ux import Unit
from libnagatofontbook.eventbox.ForLabel import NagatoEventBox


class NagatoGrid(Gtk.Grid, NagatoObject):

    def _initialize_grid(self):
        Gtk.Grid.__init__(self)
        self.set_border_width(Unit("grid-spacing"))
        self.set_row_spacing(Unit("grid-spacing"))
        self.set_column_spacing(Unit("grid-spacing"))

    def __init__(self, parent):
        self._parent = parent
        self._initialize_grid()
        self._parent.add(self)
        yuki_font_chooser_widget = Gtk.FontChooserWidget()
        yuki_font_chooser_widget.set_preview_text("YUKI.N > 見えてる？")
        self.attach(yuki_font_chooser_widget, 0, 0, 1, 1)
