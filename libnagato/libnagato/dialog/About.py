
from gi.repository import Gtk
from libnagato.dialog.ui.LabelAbout import NagatoLabelAbout
from libnagato.dialog.ui.GtkImage import NagatoGtkImage


class NagatoAboutDialog(Gtk.Dialog):

    @classmethod
    def call(self, resources):
        yuki_dialog = NagatoAboutDialog(resources)
        yuki_dialog.run()
        yuki_dialog.destroy()

    def _set_buttons(self):
        self.add_button("I see", Gtk.ResponseType.OK)

    def _set_icon(self, content_area):
        NagatoGtkImage(
            content_area,
            self._resources.get_application_icon(),
            "dialog-label-about",
            -1,
            120
            )

    def _initialize_content_area(self):
        yuki_content_area = self.get_content_area()
        yuki_content_area.set_spacing(0)
        yuki_content_area.set_border_width(8)
        self._set_icon(yuki_content_area)
        self._label = NagatoLabelAbout(yuki_content_area, self._resources)

    def __init__(self, resources):
        self._resources = resources
        Gtk.Dialog.__init__(
            self,
            "dialog: about {}".format(self._resources["name"]),
            Gtk.Window(title="About {}".format(self._resources["name"])),
            Gtk.ResponseType.OK,
            None
            )
        self.set_default_size(360, 600)
        self._initialize_content_area()
        self._set_buttons()
        self.show_all()
