
from gi.repository import Gtk
from libnagatoterminal.dialog import Portal
from libnagatoterminal.dialog.ui.LabelAbout import NagatoLabelAbout


class NagatoAboutDialog(Gtk.Dialog):

    def _set_buttons(self):
        self.add_button("OK", Gtk.ResponseType.OK)

    def _initialize_content_area(self):
        yuki_content_area = self.get_content_area()
        yuki_content_area.set_spacing(8)
        yuki_content_area.set_border_width(8)
        self._label = NagatoLabelAbout(yuki_content_area)

    def set_processes(self, processes):
        self._label.set_processes(processes)

    def __init__(self):
        Gtk.Dialog.__init__(
            self,
            "dialog: about",
            Gtk.Window(title="About nagato-terminal"),
            Gtk.ResponseType.OK,
            None
            )
        self.set_default_size(500, 500)
        self._initialize_content_area()
        self._set_buttons()
        self.show_all()

