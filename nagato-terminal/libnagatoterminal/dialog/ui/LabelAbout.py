
from gi.repository import Gtk


class NagatoLabelAbout(Gtk.Label):

    def _get_message(self):
        yuki_message = \
            "<big>nagato-terminal</big>\n"\
            "\n"\
            "A multi grid terminal emulator.\n"\
            "This software is licensed under S.O.S. License.\n"\
            "\n"\
            "Copyright (C) 2017 takeda.nemuru\n"\
            "&lt;takeda.nemuru@yandex.com&gt;\n"\
            "\n"
        return yuki_message

    def __init__(self, content_area):
        Gtk.Label.__init__(self)
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.get_style_context().add_class("dialog-label-about")
        self.set_markup(self._get_message())
        content_area.add(self)
