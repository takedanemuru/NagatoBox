
from gi.repository import Gtk
from libnagatoterminal.dialog import Portal
from libnagatoterminal.dialog.ui.LabelAbout import NagatoLabelAbout
from libnagatoterminal.Resources import NagatoResources
from libnagatoterminal.dialog.ui.GtkImage import NagatoGtkImage


class NagatoAboutDialog(Gtk.Dialog):

    def _set_buttons(self):
        self.add_button("I see", Gtk.ResponseType.OK)

    def _set_icon(self, content_area):
        yuki_resources = NagatoResources()
        NagatoGtkImage(
            content_area,
            yuki_resources.get_application_icon(),
            "dialog-label-about",
            -1,
            120
            )

    def _initialize_content_area(self):
        yuki_content_area = self.get_content_area()
        yuki_content_area.set_spacing(0)
        yuki_content_area.set_border_width(8)
        self._set_icon(yuki_content_area)
        self._label = NagatoLabelAbout(yuki_content_area)

    def set_processes(self, processes):
        self._label.set_processes(processes)

    def __init__(self):
        Gtk.Dialog.__init__(
            self,
            "dialog: about nagato-terminal",
            Gtk.Window(title="About nagato-terminal"),
            Gtk.ResponseType.OK,
            None
            )
        self.set_default_size(360, 600)
        self._initialize_content_area()
        self._set_buttons()
        self.show_all()
