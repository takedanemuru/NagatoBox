
from gi.repository import Gtk
from libnagatoterminal import GdkPixbufIcon

class NagatoAboutDialog2(Gtk.AboutDialog):

    def _initialize_gtk_box(self):
        yuki_box = self.get_content_area()
        yuki_box_2 = yuki_box.get_children()[0]
        yuki_box_2.get_style_context().add_class("about-dialog-label")
        yuki_box_2.set_opacity(0.7)
        yuki_box_2.set_spacing(8)
        yuki_box_2.set_border_width(8)
        return yuki_box_2

    def __init__(self):
        Gtk.AboutDialog.__init__(self)
        self.set_logo(GdkPixbufIcon.get_application_icon())
        self.set_license("S.O.S. License")
        yuki_box_2 = self._initialize_gtk_box()
        yuki_message = \
            "<big><b>nagato-terminal</b></big>\n"\
            "\n"\
            "A multi-grid terminal emulator\n"\
            "This software is now under heavy construction\n"\
            "\n"\
            "A multi-grid terminal emulator\n"\
            "This software is now under heavy construction\n"\
            "\n"\
            "A multi-grid terminal emulator\n"\
            "This software is now under heavy construction\n"
        yuki_image = yuki_box_2.get_children()[0]
        yuki_image.set_property("height-request", 100)
        yuki_label = yuki_box_2.get_children()[1]
        yuki_label.set_text("foo bar baz")
        yuki_label.set_markup(yuki_message)
        yuki_label.set_justify(Gtk.Justification.CENTER)
        yuki_label.get_style_context().add_class("about-dialog-label")
        self.show_all()
