
from gi.repository import Gtk
from libnagatoterminal.gdk import PixbufIcon
from libnagatoterminal.dialog.ui.GtkBoxAbout import NagatoGtkBoxAbout

class NagatoAboutDialog(Gtk.AboutDialog):

    def _initialize_label(self, label):
        yuki_message = \
            "<big><b>nagato-terminal</b></big>\n"\
            "\n"\
            "A multi-grid terminal emulator\n"
        label.set_markup(yuki_message)
        label.set_justify(Gtk.Justification.CENTER)
        label.get_style_context().add_class("about-dialog-label")

    def __init__(self):
        Gtk.AboutDialog.__init__(self)
        self.set_logo(PixbufIcon.get_application_icon())
        self.set_license("S.O.S. License")
        yuki_gtk_box = NagatoGtkBoxAbout(self.get_content_area())
        yuki_image = yuki_gtk_box.get_gtk_image()
        yuki_image.set_property("height-request", 100)
        self._initialize_label(yuki_gtk_box.get_gtk_label())
        self.show_all()
